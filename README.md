# FlyRank ML Internship — Applied Search Intelligence

## CTR Opportunity Prioritization

A machine-learning project that uses anonymized FlyRank Google Search performance data to identify and prioritize pages with potential click-through-rate (CTR) opportunities.

The project follows a reproducible search-intelligence workflow:

**problem framing → data understanding → feature engineering → baseline → model training → validation → ranking → actionable recommendations**

For V2, the project adds a natural-language agent layer that makes the generated ranking outputs easier to explore and understand through ordinary questions.

---

# 🎯 The Problem

Search and content teams may have many pages that receive search impressions but do not capture clicks at the same rate as other visible pages.

The practical question is:

> **"Which pages should we investigate first for potential CTR improvement?"**

This project treats CTR opportunity prioritization as a ranking and decision-support problem.

Rather than attempting to predict Google's ranking algorithm or guarantee future traffic gains, the workflow identifies pages that appear to have potential click-capture opportunities based on the available search-performance signals.

The goal is to help an SEO or content team decide where to focus investigation first.

The system is designed to support human decision-making — not replace SEO judgment or claim causal impact from a recommended change.


---

# 🚀 What I Built

The project contains a reproducible machine-learning workflow that:

1. Loads anonymized FlyRank Google Search performance data.
2. Prepares the available search-performance signals.
3. Builds features related to visibility and click-through performance.
4. Creates a transparent baseline for identifying CTR opportunities.
5. Trains a machine-learning model to rank opportunity candidates.
6. Evaluates the learned model against the baseline.
7. Produces a ranked CTR opportunity queue.
8. Exports the results for analysis and human review.
9. Adds a V2 natural-language agent for exploring the generated outputs.

The final output is a practical **CTR opportunity prioritization system**.

The recommendations are intended as investigation priorities. They do not guarantee that changing a page will increase its future CTR or search performance.


---

# 📊 Key Result

The project compares a transparent baseline against a learned Decision Tree model for prioritizing CTR opportunities.

The evaluation uses Precision@50 to answer the practical question:

> **"If the team can only investigate the top 50 pages, how many of those pages are identified as relevant opportunities?"**

The model substantially improves the ranking of the selected opportunity class compared with the baseline on the evaluation split.

The exact results, evaluation design, and charts are presented in the deployed research paper.

### What this means

The model should not be interpreted as a causal predictor of future CTR.

The result demonstrates that the learned ranking approach can prioritize the defined opportunity signal more effectively than the baseline on the evaluated data.

This is therefore a **decision-support result**, not evidence that the model can predict Google's future rankings or guarantee improvements after a content change.

---

# 🧠 Machine-Learning Workflow

The project follows a transparent CTR opportunity-ranking pipeline:

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
                  CTR Baseline
                         │
                         ▼
                  Model Training
                         │
                         ▼
                    Validation
                         │
                         ▼
              Ranked CTR Opportunities
                         │
                         ▼
               Opportunity Queue
                         │
                         ▼
             V2 Natural-Language Agent
                         │
                         ▼
                 Human Decision
```

The analytical pipeline generates the evidence and ranking.

The conversational layer sits on top of those outputs and makes them easier to explore.

The system therefore separates:

**data and ML analysis → ranked evidence → natural-language exploration → human review**


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

V2 adds a natural-language interaction layer over the CTR opportunity-ranking outputs.

Instead of manually opening the generated CSV and searching through rows, a user can ask questions such as:

```text
What are the top CTR opportunities?
```

```text
Which pages should we investigate first?
```

```text
Explain the highest-priority opportunities.
```

```text
What does the ranked opportunity queue contain?
```

The goal is to make the analytical results easier for a non-technical SEO or content user to explore.

### Important design choice

The agent does **not** replace the machine-learning pipeline.

The architecture remains:

```text
Search data
    ↓
CTR analysis / ML pipeline
    ↓
Ranked opportunity output
    ↓
Natural-language agent
    ↓
Human-readable answer
```

This keeps the underlying analysis reproducible and allows the generated results to be inspected independently of the conversational interface.


---

# 📁 Repository Structure

```text
flyrank-ml-work/
│
├── README.md
├── retrospective.md              
├── requirements.txt
│
├── data/
├── docs/
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
├── submission/
│   ├── README.md
│   └── paper_url.txt
│
└── work/
    ├── README.md
    ├── capstone_report_template.md
    └── notebooks/
        ├── capstone.ipynb
        ├── w01_research_question.ipynb
        ├── w02_ml_task_framing.ipynb
        ├── w03_data_contract.ipynb
        ├── w03_feature_leakage_check.ipynb
        ├── w04_baseline_score.ipynb
        ├── w04_signal_audit.ipynb
        ├── w05_model.ipynb
        ├── w06_validation_audit.ipynb
        └── w07_action_playbook.ipynb
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

# 📈 Ranked CTR Opportunity Queue

One of the main outputs of the project is:

```text
outputs/refresh_queue_sample.csv
```

The generated output contains ranked opportunity records that can be reviewed by an SEO or content team.

The queue includes ranking fields such as:

```text
final_rank
content_id
```

along with the feature and scoring information used to describe each opportunity.

The purpose of the queue is not to prescribe a guaranteed content change. It provides a prioritized list of pages that deserve further investigation for potential CTR improvement.

A high-ranked page is therefore an **opportunity for human review**, not a guaranteed optimization target.


---

# 🧪 Evaluation Philosophy

The project evaluates the system according to the decision it is intended to support:

> **If a team can only investigate a limited number of pages, does the model place relevant CTR opportunities near the top of the queue?**

For this reason, ranking-oriented evaluation such as **Precision@50** is used.

The learned model is compared against a transparent baseline on the same evaluation setup.

The important distinction is that the evaluation measures prioritization of the defined opportunity signal. It does not establish that a recommended page change will cause future CTR improvement.

The results should therefore be interpreted as:

**observed → measured → directional → decision-support**

rather than as a causal or guaranteed SEO prediction.

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

This system is a **CTR opportunity decision-support tool**, not an autonomous SEO system.

A highly ranked page represents an opportunity for human investigation. It does not guarantee that changing the page will improve future CTR, traffic, rankings, or conversions.

Important limitations include:

1. The opportunity definition is based on the available search-performance signals and therefore depends on the assumptions used to construct the target.
2. Historical relationships do not guarantee future performance.
3. Search performance can change because of factors outside the modeled features.
4. The available dataset represents a particular observation window and may not generalize to every site or future period.
5. The natural-language agent depends on the generated analytical outputs being available and up to date.
6. Human SEO judgment is still required before making or prioritizing actual content changes.
7. The evaluation demonstrates prioritization performance on the defined evaluation data; it does not establish causal CTR improvement.

The model therefore answers:

> **"Which pages should we investigate first for potential CTR opportunity?"**

rather than:

> **"Which pages are guaranteed to improve?"**

---

# 🔮 Future Work

Potential V3 improvements include:

* connecting the agent to live search-performance data
* adding richer explanations for individual CTR opportunity rankings
* adding confidence or uncertainty indicators
* evaluating recommendations against future search-performance windows
* tracking whether investigated pages subsequently experience measurable changes
* adding human-review feedback to the prioritization workflow
* supporting richer natural-language analytical questions
* adding a lightweight web dashboard

The most valuable next step would be closing the measurement loop:

```text
CTR opportunity identified
          ↓
Human investigation
          ↓
Content / metadata decision
          ↓
Future search performance
          ↓
Measure observed change
          ↓
Improve prioritization
```

This would help distinguish simple opportunity ranking from evidence about what happens after an intervention.

---

# 📄 Research Paper

The capstone research paper is the deeper explanation of the project's research question, methodology, analysis, results, and conclusions.

The paper URL is maintained in:

Live paper: https://quratulainazhar22.github.io/flyrank-ml-work/

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
Broken down as:

142.5 hours — assignments
1.5 hours — event/recording
2 hours — Anthropic Academy course
0 hours currently — capstone because it is still in review
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
* **Capstone:** CTR Opportunity Prioritization using anonymized FlyRank Google Search performance data
* **Ranked Refresh Queue:** `outputs/refresh_queue_sample.csv`
* **Model Report:** `outputs/model_report.md`
* **V2 Natural-Language Agent:** Natural-language interface over the generated ranking outputs

### Documentation & Demo

* **README:** This document
* **Demo Video:** https://youtu.be/ffVSCyl3M94

### Final Reflection
* **Research Paper:**
https://quratulainazhar22.github.io/flyrank-ml-work/

* **Retrospective:** 500–800 word reflection on the project, changes in approach, lessons learned, and future direction

### Public Proof

* **Build-in-Public Post:** http://youtube.com/post/Ugkxs5K5A8sHOMR8HBLGcnfLBy-YmYkWYPYy

### Final Administrative Deliverables

* **Hours Log:** Completed in the FlyRank portal with 146 hours + Capstone hours remain pending until the capstone is accepted through the FlyRank review process.
* **Personal Site:** Published on the required FlyRank domain
* **Final Review:** Submitted for human review and sign-off

# 🤖 AI Transparency

I used AI tools, including Claude and ChatGPT, as development and thinking partners during this project. They helped with code suggestions, debugging, documentation, brainstorming, and refining the natural-language agent.

I personally reviewed, tested, and validated the implementation, model workflow, evaluation outputs, documentation, and project claims before including them in the final submission.

AI was used as an assistance and reasoning tool; the final project structure, validation decisions, outputs, and interpretation were reviewed by me.

---

## FlyRank ML Internship

**Track:** Machine Learning
**Project:** Applied Search Intelligence
**Focus:** Google Search Ranking & Content Refresh Prioritization
**V2:** Natural-Language Agent
