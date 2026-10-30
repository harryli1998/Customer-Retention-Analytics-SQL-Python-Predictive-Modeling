# Customer Retention Analytics

Reproducible portfolio project exploring churn drivers and retention prioritization using **Python, SQL and predictive modeling**.

## Data provenance
**Synthetic data only.** No actual customers, clients, historical work, or commercial results are represented. Generated with a fixed random seed.

## Run
```bash
pip install -r requirements.txt
python src/generate_data.py
python src/analyze.py
python src/model.py
pytest -q
```

## Contents
- `src/generate_data.py`: reproducible synthetic dataset
- `src/analyze.py`: descriptive KPIs and plan-level churn
- `src/model.py`: stratified train/test evaluation, baseline and logistic regression
- `sql/retention_analysis.sql`: SQLite-compatible analytical queries
- `tests/test_pipeline.py`: data integrity and pipeline tests
- `docs/business_recommendations.md`: actionable interpretation and limitations

## Methodological limitations
This is a demonstration, not a client engagement. Cross-sectional synthetic records do not support temporal cohort retention, causal effects, or measured intervention ROI. A churn score is not an uplift score. For real use, validate feature timing, calibration, fairness, and retention intervention effectiveness with randomized tests.

## Employment history
Repository creation and commits reflect actual creation dates and do not establish past OPT employment or work hours.
