from pathlib import Path
import pandas as pd


# Find the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Existing FlyRank output
QUEUE_PATH = PROJECT_ROOT / "outputs" / "refresh_queue_sample.csv"
REPORT_PATH = PROJECT_ROOT / "outputs" / "model_report.md"


def load_queue():
    """Load the FlyRank content opportunity queue."""
    if not QUEUE_PATH.exists():
        raise FileNotFoundError(
            f"Could not find the queue file: {QUEUE_PATH}"
        )

    return pd.read_csv(QUEUE_PATH)


def get_top_opportunities(n=10):
    """Return the highest-ranked content opportunities."""

    df = load_queue()

    # Sort by final rank if available
    if "final_rank" in df.columns:
        result = df.sort_values("final_rank").head(n)
    else:
        result = df.sort_values(
            "final_refresh_score",
            ascending=False
        ).head(n)

    columns = [
        "final_rank",
        "content_id",
        "final_refresh_score",
        "confidence",
        "suggested_action",
        "final_reason_codes",
        "impressions_90d",
        "ctr",
        "avg_position",
    ]

    # Keep only columns that actually exist
    columns = [c for c in columns if c in result.columns]

    return result[columns]


def get_high_confidence(n=10):
    """Return high-confidence content opportunities."""

    df = load_queue()

    if "confidence" not in df.columns:
        return pd.DataFrame()

    result = df[
        df["confidence"]
        .astype(str)
        .str.lower()
        .eq("high")
    ]

    if "final_rank" in result.columns:
        result = result.sort_values("final_rank")

    return result.head(n)


def explain_opportunity(rank):
    """Explain why a particular ranked opportunity was recommended."""

    df = load_queue()

    if "final_rank" not in df.columns:
        return None

    matches = df[df["final_rank"] == rank]

    if matches.empty:
        return None

    row = matches.iloc[0]

    explanation = {
        "rank": row.get("final_rank"),
        "content_id": row.get("content_id"),
        "refresh_score": row.get("final_refresh_score"),
        "confidence": row.get("confidence"),
        "suggested_action": row.get("suggested_action"),
        "reason_codes": row.get("final_reason_codes"),
        "impressions_90d": row.get("impressions_90d"),
        "clicks_90d": row.get("clicks_90d"),
        "sessions_90d": row.get("sessions_90d"),
        "avg_position": row.get("avg_position"),
        "ctr": row.get("ctr"),
        "content_age_days": row.get("content_age_days"),
        "days_since_last_update": row.get("days_since_last_update"),
        "word_count": row.get("word_count"),
        "trend_direction": row.get("trend_direction"),
        "content_type": row.get("content_type"),
        "main_intent": row.get("main_intent"),
    }

    return explanation


def get_queue_summary():
    """Return basic information about the current queue."""

    df = load_queue()

    summary = {
        "rows_available": len(df),
        "columns_available": len(df.columns),
    }

    if "confidence" in df.columns:
        summary["high_confidence"] = int(
            df["confidence"]
            .astype(str)
            .str.lower()
            .eq("high")
            .sum()
        )

    if "final_refresh_score" in df.columns:
        summary["highest_refresh_score"] = float(
            df["final_refresh_score"].max()
        )

    if "suggested_action" in df.columns:
        summary["actions"] = (
            df["suggested_action"]
            .value_counts()
            .to_dict()
        )

    return summary


def get_model_summary():
    """Read the existing FlyRank model report."""

    if not REPORT_PATH.exists():
        return "The model report was not found."

    text = REPORT_PATH.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    # Return the existing report rather than inventing new metrics.
    return text