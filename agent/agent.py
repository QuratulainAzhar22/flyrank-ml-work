import re

from tools import (
    get_top_opportunities,
    get_high_confidence,
    explain_opportunity,
    get_queue_summary,
    get_model_summary,
)


def print_opportunities(df, title):
    """Display opportunity results in a readable format."""

    print()
    print("=" * 70)
    print(title)
    print("=" * 70)

    if df.empty:
        print("No matching opportunities were found.")
        return

    for _, row in df.iterrows():
        print()
        print(f"Rank: {row.get('final_rank', 'N/A')}")
        print(f"Content ID: {row.get('content_id', 'N/A')}")
        print(f"Refresh score: {row.get('final_refresh_score', 'N/A')}")
        print(f"Confidence: {row.get('confidence', 'N/A')}")
        print(f"Suggested action: {row.get('suggested_action', 'N/A')}")
        print(f"Reasons: {row.get('final_reason_codes', 'N/A')}")
        print(f"Impressions: {row.get('impressions_90d', 'N/A')}")
        print(f"CTR: {row.get('ctr', 'N/A')}")
        print(f"Average position: {row.get('avg_position', 'N/A')}")


def extract_number(text, default=10):
    """Extract a number from the user's request."""

    match = re.search(r"\b(\d+)\b", text)

    if match:
        return int(match.group(1))

    return default


def detect_intent(text):
    """
    Decide which tool should handle the user's request.

    Returns:
        intent name
        optional number
    """

    text = text.lower().strip()

    # Exit requests
    if text in {"exit", "quit", "bye", "q"}:
        return "exit", None

    # Explanation requests
    explanation_words = [
        "why",
        "explain",
        "reason",
        "reasons",
        "recommend",
    ]

    if any(word in text for word in explanation_words):
        rank = extract_number(text, default=None)

        if rank is not None:
            return "explain", rank

        return "explain", None

    # Model performance requests
    model_words = [
        "model",
        "performance",
        "accuracy",
        "f1",
        "precision",
        "evaluation",
        "evaluate",
        "how did",
    ]

    if any(word in text for word in model_words):
        return "model", None

    # High-confidence requests
    confidence_words = [
        "high confidence",
        "high-confidence",
        "confident",
        "confidence",
    ]

    if any(word in text for word in confidence_words):
        return "high_confidence", extract_number(text)

    # Summary requests
    summary_words = [
        "summary",
        "summarize",
        "overview",
        "how many",
        "queue size",
        "total",
    ]

    if any(word in text for word in summary_words):
        return "summary", None

    # Top opportunity requests
    top_words = [
        "top",
        "highest",
        "priority",
        "prioritize",
        "review first",
        "opportunities",
        "pages should i review",
    ]

    if any(word in text for word in top_words):
        return "top", extract_number(text)

    return "unknown", None


def handle_request(user_input):
    """Route a natural-language request to the correct tool."""

    intent, number = detect_intent(user_input)

    # --------------------------------------------------
    # TOP OPPORTUNITIES
    # --------------------------------------------------

    if intent == "top":

        # Prevent accidentally requesting hundreds of rows
        number = min(number, 20)

        results = get_top_opportunities(number)

        print_opportunities(
            results,
            f"TOP {number} CONTENT OPPORTUNITIES"
        )

        return

    # --------------------------------------------------
    # HIGH CONFIDENCE
    # --------------------------------------------------

    if intent == "high_confidence":

        number = min(number, 20)

        results = get_high_confidence(number)

        print_opportunities(
            results,
            f"TOP {number} HIGH-CONFIDENCE OPPORTUNITIES"
        )

        return

    # --------------------------------------------------
    # EXPLAIN
    # --------------------------------------------------

    if intent == "explain":

        if number is None:
            print()
            print(
                "I can explain a specific opportunity. "
                "Please include its rank."
            )
            print()
            print("Example:")
            print("  Why is opportunity 3 recommended?")
            return

        result = explain_opportunity(number)

        print()
        print("=" * 70)
        print(f"WHY IS OPPORTUNITY #{number} RECOMMENDED?")
        print("=" * 70)

        if result is None:
            print(f"No opportunity with rank {number} was found.")
            return

        labels = {
            "content_id": "Content ID",
            "refresh_score": "Refresh score",
            "confidence": "Confidence",
            "suggested_action": "Suggested action",
            "reason_codes": "Reason codes",
            "impressions_90d": "90-day impressions",
            "clicks_90d": "90-day clicks",
            "sessions_90d": "90-day sessions",
            "avg_position": "Average position",
            "ctr": "CTR",
            "content_age_days": "Content age (days)",
            "days_since_last_update": "Days since last update",
            "word_count": "Word count",
            "trend_direction": "Trend",
            "content_type": "Content type",
            "main_intent": "Main intent",
        }

        for key, label in labels.items():
            if key in result:
                print(f"{label}: {result[key]}")

        return

    # --------------------------------------------------
    # QUEUE SUMMARY
    # --------------------------------------------------

    if intent == "summary":

        summary = get_queue_summary()

        print()
        print("=" * 70)
        print("FLYRANK QUEUE SUMMARY")
        print("=" * 70)

        print(f"Rows available: {summary['rows_available']}")
        print(f"Columns available: {summary['columns_available']}")

        if "high_confidence" in summary:
            print(
                f"High-confidence opportunities: "
                f"{summary['high_confidence']}"
            )

        if "highest_refresh_score" in summary:
            print(
                f"Highest refresh score: "
                f"{summary['highest_refresh_score']:.3f}"
            )

        if "actions" in summary:
            print("\nSuggested actions:")

            for action, count in summary["actions"].items():
                print(f"  - {action}: {count}")

        return

    # --------------------------------------------------
    # MODEL REPORT
    # --------------------------------------------------

    if intent == "model":

        report = get_model_summary()

        print()
        print("=" * 70)
        print("FLYRANK MODEL EVALUATION")
        print("=" * 70)
        print()

        print(report)

        return

    # --------------------------------------------------
    # UNKNOWN REQUEST
    # --------------------------------------------------

    print()
    print("I couldn't determine what you want me to do.")
    print()
    print("Try something like:")
    print("  • Show me the top 5 opportunities")
    print("  • Which pages should I review first?")
    print("  • Show high confidence opportunities")
    print("  • Why is opportunity 3 recommended?")
    print("  • Give me a summary of the queue")
    print("  • How did the model perform?")


def main():

    print()
    print("=" * 70)
    print("       FLYRANK CONTENT OPPORTUNITY AGENT — V2")
    print("=" * 70)

    print()
    print(
        "I can analyze the FlyRank content opportunity queue."
    )

    print()
    print("Try asking me something like:")
    print("  Show me the top 5 opportunities")
    print("  Which pages should I review first?")
    print("  Why is opportunity 3 recommended?")
    print("  Show high confidence opportunities")
    print("  Give me a summary")
    print("  How did the model perform?")
    print()

    while True:

        user_input = input("You: ").strip()

        if not user_input:
            continue

        if user_input.lower() in {
            "exit",
            "quit",
            "bye",
            "q",
        }:
            print("\nAgent: Goodbye!")
            break

        print("\nAgent: Let me check the FlyRank results...")

        handle_request(user_input)


if __name__ == "__main__":
    main()