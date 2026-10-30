from src.generate_data import generate
from src.analyze import summarize
from src.model import evaluate


def test_reproducible():
    assert generate(50, 42).equals(generate(50, 42))


def test_data_integrity():
    df = generate(500)
    assert df.customer_id.is_unique
    assert df.monthly_spend.ge(0).all()
    assert set(df.churned.unique()).issubset({0, 1})


def test_analysis_and_model():
    df = generate(500)
    overall, segments = summarize(df)
    assert overall.loc[0, 'customers'] == 500
    assert segments.customers.sum() == 500
    metrics = evaluate(df)
    assert len(metrics) == 2
    assert metrics.roc_auc.between(0, 1).all()
