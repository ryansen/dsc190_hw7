# Assignment 07 – Reproducible Data Pipelines

A three-stage DVC pipeline that cleans, transforms, and enriches a raw event log, plus a Marimo notebook that visualises the results.

## Quick start

```bash
# 1. Clone and enter the repo
git clone <your-repo-url>
cd assignment07

# 2. Create and activate the virtual environment
uv sync
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Run the full pipeline
dvc repro

# 4. Open the notebook
marimo run notebooks/report.py
# or edit it interactively:
marimo edit notebooks/report.py
```

## Pipeline stages

| Stage | Input | Output |
|-------|-------|--------|
| `clean` | `data/raw/events.csv` | `data/clean/events.csv` |
| `transform` | `data/clean/events.csv` | `data/transformed/events.csv` |
| `features` | `data/transformed/events.csv` | `data/features/events.csv` |

## Project layout

```
assignment07/
├── data/
│   └── raw/events.csv        ← committed to git
├── notebooks/
│   └── report.py             ← Marimo notebook
├── src/
│   ├── clean.py
│   ├── transform.py
│   └── features.py
├── dvc.yaml
├── pyproject.toml
└── README.md
```
