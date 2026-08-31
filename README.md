# FlyRank ML Internship — Applied Search Intelligence

## Google Search Ranking & Content Refresh Prioritization

A machine-learning project that turns anonymized Google Search performance data into a **ranked content-refresh queue**, helping SEO and content teams identify which pages deserve attention first.

The project follows a complete ML workflow:

**problem framing → data understanding → feature engineering → baseline → model training → validation → ranking → actionable recommendations**

For V2, the project adds a **natural-language agent layer** that makes the generated ranking outputs easier to explore and understand through ordinary questions.

---

## 🎯 The Problem

SEO and content teams can have thousands of pages competing for limited optimization time.

The practical question is not simply:

> "Which pages perform badly?"

It is:

> **"Which pages should we review and refresh first?"**

This project treats content refresh prioritization as a ranking/decision-support problem.

Instead of manually inspecting pages one by one, the workflow uses search-performance signals to generate a prioritized review queue.

The system is designed to support human decision-making — not to replace SEO judgment or claim to predict Google's algorithm.

---

# 🚀 What I Built

The project contains a reproducible machine-learning workflow that:

1. Loads anonymized FlyRank search data.
2. Cleans and prepares the available signals.
3. Builds a feature representation for content opportunities.
4. Creates a transparent baseline scoring rule.
5. Trains machine-learning models.
6. Evaluates the models using ranking-oriented metrics.
7. Produces a ranked content-refresh queue.
8. Exports results for further analysis and review.
9. Adds a V2 natural-language interface for querying the generated outputs.

The final output is a practical **content refresh prioritization system**.

---

# 📊 Key Result

The project compares a simple hand-written baseline against the learned model.

On the bundled evaluation workflow:

| Approach      | Precision@50 |
| ------------- | -----------: |
| Baseline rule |       ≈ 0.24 |
| Learned model |       ≈ 0.74 |

The exact model score can vary slightly depending on the environment and library versions.

The important finding is the substantial improvement in the ability to identify relevant pages near the top of the review queue.

### What this means

The model is not simply producing a prediction for every page.

It is being evaluated according to the practical question:

> **"If the team only has time to review the top 50 pages, how many of those pages are actually useful opportunities?"**

That makes Precision@50 a useful metric for this decision-support task.

---

# 🧠 Machine-Learning Workflow

The project follows a transparent pipeline:

```text
                    FlyRank Search Data
                            │
                            ▼
                  Data Preparation
                            │
                            ▼
                  Feature Engineering
                            │
                            ▼
                  Baseline Scoring
                            │
                            ▼
                   Model Training
                            │
                            ▼
                     Evaluation
                            │
                            ▼
                 Ranked Opportunities
                            │
                            ▼
                Content Refresh Queue
                            │
                            ▼
             V2 Natural-Language Agent
                            │
                            ▼
                    Human Decision
```

The important design principle is that the conversational layer sits **on top of the analytical workflow**.

The ML pipeline generates the evidence.

The agent makes that evidence easier to explore.

---

# 🔬 Pipeline Scripts

The main pipeline is implemented in `scripts/`.

| Script                      | Purpose                                                        |
| --------------------------- | -------------------------------------------------------------- |
| `01_prepare_features.py`    | Cleans data, prepares features, and defines the modeling frame |
| `02_baseline_score.py`      | Creates a transparent baseline prioritization score            |
| `03_train_model.py`         | Trains the machine-learning models                             |
| `04_evaluate_and_export.py` | Evaluates the model and exports ranked results                 |
| `05_build_pdf_report.py`    | Builds a shareable PDF report                                  |
| `ml_utils.py`               | Shared utilities used by the pipeline                          |
| `run_all.py`                | Runs the complete workflow                                     |

The overall workflow is:

```text
01_prepare_features
        ↓
02_baseline_score
        ↓
03_train_model
        ↓
04_evaluate_and_export
        ↓
05_build_pdf_report
```

---

# 🤖 V2 — Natural-Language Agent

V2 adds a natural-language interaction layer over the existing ML outputs.

Instead of manually opening the generated CSV and searching through rows, a user can ask questions such as:

```text
What are the top content opportunities?
```

```text
Which pages should we refresh first?
```

```text
Explain the highest-priority opportunities.
```

```text
What does the ranked refresh queue contain?
```

The goal of the agent is to make the analytical results more accessible to a non-technical user.

### Important design choice

The agent does **not** replace the machine-learning pipeline.

The architecture remains:

```text
Search data
    ↓
ML pipeline
    ↓
Ranked output
    ↓
Agent
    ↓
Natural-language answer
```

This keeps the underlying analysis reproducible and allows the generated results to be inspected independently of the conversational interface.

---

# 📁 Repository Structure

```text
flyrank-ml-work/
│
├── retrospective.md
├── README.md
├── requirements.txt
│
├── data/
│   └── raw/
│
├── docs/
│   ├── ml-core-foundation-framework.md
│   └── ml-intern-dataset-and-lane-guide.md
│
├── notebooks/
│   ├── 01_first_look_and_discovery.ipynb
│   ├── 02_your_first_readable_model.ipynb
│   └── 03_working_with_the_full_release.ipynb
│
├── outputs/
│   ├── model_report.md
│   └── refresh_queue_sample.csv
│
├── scripts/
│   ├── 01_prepare_features.py
│   ├── 02_baseline_score.py
│   ├── 03_train_model.py
│   ├── 04_evaluate_and_export.py
│   ├── 05_build_pdf_report.py
│   ├── ml_utils.py
│   └── run_all.py
│
├── skills/
│   └── README.md
│
├── submission/
│   ├── README.md
│   └── paper_url.txt
│
└── work/
    ├── README.md
    └── capstone_report_template.md
```

---

# 📂 Important Files

### `notebooks/`

The initial FlyRank learning and discovery notebooks.

They cover the early stages of the internship workflow, including:

* initial data exploration
* first readable models
* working with the larger data release

### `scripts/`

The reproducible reference pipeline used to prepare data, create a baseline, train models, evaluate results, and generate outputs.

### `outputs/`

Generated project artifacts.

The repository currently includes:

```text
model_report.md
refresh_queue_sample.csv
```

The refresh queue sample provides a concrete example of the ranked output produced by the workflow.

### `work/`

The workspace for the internship's applied work and capstone materials.

### `submission/`

Submission-specific materials, including the submission README and research-paper URL.

### `docs/`

Reference material covering the ML framework, dataset, lane guidance, and internship workflow.

---

# ⚡ Quickstart

## 1. Clone the repository

```bash
git clone https://github.com/QuratulainAzhar22/flyrank-ml-work.git
cd flyrank-ml-work
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the pipeline

```bash
python scripts/run_all.py
```

The pipeline prepares the data, creates the baseline, trains the model, evaluates the results, and generates the project outputs.

---

# 💻 Google Colab

The initial notebooks can also be opened and executed through Google Colab.

### Notebook 1 — First Look & Discovery

[Open `01_first_look_and_discovery.ipynb` in Colab](https://colab.research.google.com/github/QuratulainAzhar22/flyrank-ml-work/blob/main/notebooks/01_first_look_and_discovery.ipynb?flush_cache=true)

### Notebook 2 — First Readable Model

[Open `02_your_first_readable_model.ipynb` in Colab](https://colab.research.google.com/github/QuratulainAzhar22/flyrank-ml-work/blob/main/notebooks/02_your_first_readable_model.ipynb?flush_cache=true)

### Notebook 3 — Full Release

[Open `03_working_with_the_full_release.ipynb` in Colab](https://colab.research.google.com/github/QuratulainAzhar22/flyrank-ml-work/blob/main/notebooks/03_working_with_the_full_release.ipynb?flush_cache=true)

---

# 📈 Ranked Refresh Queue

One of the main outputs is:

```text
outputs/refresh_queue_sample.csv
```

The sample contains:

```text
200 rows × 28 columns
```

Important ranking fields include:

```text
final_rank
content_id
```

along with the feature and scoring information used to describe each opportunity.

The purpose of this output is to transform model results into a practical queue that can be reviewed by an SEO or content team.

---

# 🧪 Evaluation Philosophy

The project emphasizes evaluation based on the **actual decision the system is intended to support**.

Rather than focusing only on generic classification metrics, the workflow asks:

> If a team can only review a limited number of pages, does the model put useful opportunities near the top?

This is why ranking-oriented evaluation such as **Precision@50** is important.

The project also compares the learned model against a transparent baseline.

This provides a useful sanity check:

```text
Simple rule
    ↓
How well does it prioritize?

ML model
    ↓
Does learning improve the prioritization?
```

The model is valuable only if it improves the decision being supported.

---

# 🛡️ Data Safety

This project uses anonymized FlyRank data.

The repository should not contain:

* private client information
* client names
* private domains
* private URLs
* private keywords
* credentials
* confidential exports

Do not add private client data to this repository.

Do not paste private client data into third-party AI tools.

Results should be described carefully as:

* observed
* measured
* directional
* decision-support

The project does **not** claim to predict Google's ranking algorithm.

---

# ⚠️ Limitations

This system is a **decision-support tool**, not an autonomous SEO system.

A high-ranked page is an opportunity for human review, not a guarantee that changing the page will improve its future search performance.

There are several important limitations:

1. Search performance can change for many reasons outside the modeled features.
2. Historical relationships do not guarantee future outcomes.
3. The ranked queue depends on the quality and availability of the underlying data.
4. The natural-language agent depends on the generated project outputs being available and up to date.
5. Human SEO judgment is still required before making content changes.

The model therefore answers:

> **"Which pages should we investigate first?"**

rather than:

> **"Which pages are guaranteed to improve?"**

---

# 🔮 Future Work

Potential V3 improvements include:

* connecting the agent to live search-performance data
* adding richer explanations for individual rankings
* adding confidence or uncertainty indicators
* comparing performance before and after content refreshes
* tracking whether recommended refreshes produce measurable gains
* supporting more complex natural-language analytical questions
* adding a lightweight web dashboard
* introducing feedback from human reviewers into the prioritization workflow

The most valuable next step would be closing the loop:

```text
Recommendation
      ↓
Content refresh
      ↓
Future search performance
      ↓
Measure outcome
      ↓
Improve prioritization
```

---

# 📄 Research Paper

The capstone research paper is the deeper explanation of the project's research question, methodology, analysis, results, and conclusions.

The paper URL is maintained in:

```text
submission/paper_url.txt
```

---

# 🎥 Demo

The recommended demonstration follows this workflow:

```text
1. Introduce the search-intelligence problem
2. Show the ML pipeline
3. Show the generated refresh queue
4. Demonstrate the V2 natural-language agent
5. Explain the architecture
6. State the limitation honestly
```

The key demonstration is showing that a user can move from:

```text
"Here is a large search dataset."
```

to:

```text
"Here are the pages the model recommends reviewing first."
```

and finally:

```text
"Let me ask the system why these opportunities matter."
```

---
# 📝 Retrospective

500–800 word retrospective: retrospective.md

The retrospective explains what I set out to build, how the project evolved, what I would build next, and the three most transferable lessons from the internship.


# 🌐 Personal Portfolio

Live portfolio: https://quratulainazhar22.github.io/

The portfolio presents my projects, skills, and professional work.

# ⏱️ Internship Hours

The FlyRank portal currently records 146 estimated hours, including completed assignments, an attended event/recording, and a verified Anthropic Academy course.

Capstone hours remain pending until the capstone is accepted through the FlyRank review process.

# 📢 Build-in-Public Post

Public project post: http://youtube.com/post/Ugkxs5K5A8sHOMR8HBLGcnfLBy-YmYkWYPYy

The post shares the project journey, including a real design decision and an important limitation of the system.

# 🏁 Final Takeaway

This project combines **machine learning, search intelligence, ranking, and natural-language interaction** into one workflow.

The core contribution is not simply training a model.

It is building a reproducible path from:

```text
Raw search data
      ↓
Problem framing
      ↓
Feature engineering
      ↓
Baseline
      ↓
Machine learning
      ↓
Evaluation
      ↓
Ranked content opportunities
      ↓
Natural-language exploration
      ↓
Human action
```

The result is a practical system for helping content teams decide **what to review first**, while keeping the underlying evidence visible and the final decision with a human.

---

## 📦 Final Submission Package

This repository contains the complete final submission for my FlyRank ML Internship capstone.

### Project

* **Research Paper:** `submission/paper_url.txt`
* **Capstone:** End-to-end applied Search Intelligence project
* **Ranked Refresh Queue:** `outputs/refresh_queue_sample.csv`
* **Model Report:** `outputs/model_report.md`
* **V2 Natural-Language Agent:** Natural-language interface over the generated ranking outputs

### Documentation & Demo

* **README:** This document
* **Demo Video:** https://youtu.be/ffVSCyl3M94

### Final Reflection

* **Retrospective:** 500–800 word reflection on the project, changes in approach, lessons learned, and future direction

### Public Proof

* **Build-in-Public Post:** http://youtube.com/post/Ugkxs5K5A8sHOMR8HBLGcnfLBy-YmYkWYPYy

### Final Administrative Deliverables

* **Hours Log:** Completed in the FlyRank portal 146 hours
* **Personal Site:** Published on the required FlyRank domain
* **Final Review:** Submitted for human review and sign-off


## FlyRank ML Internship

**Track:** Machine Learning
**Project:** Applied Search Intelligence
**Focus:** Google Search Ranking & Content Refresh Prioritization
**V2:** Natural-Language Agent
