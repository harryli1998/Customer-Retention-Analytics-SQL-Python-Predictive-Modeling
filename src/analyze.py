"""Descriptive customer retention KPIs."""
from pathlib import Path
import pandas as pd


def summarize(df):
    overall = pd.DataFrame([{'customers': len(df),
        'churn_rate': df.churned.mean(),
        'monthly_revenue_proxy': df.monthly_spend.sum(),
        'revenue_at_risk_proxy': df.loc[df.churned.eq(1), 'monthly_spend'].sum()}])
    segments = (df.groupby('plan', as_index=False)
        .agg(customers=('customer_id', 'size'), churn_rate=('churned', 'mean'),
             avg_monthly_spend=('monthly_spend', 'mean')))
    return overall, segments


if __name__ == '__main__':
    overall, segments = summarize(pd.read_csv('data/customers.csv'))
    Path('outputs').mkdir(exist_ok=True)
    overall.to_csv('outputs/overall_kpis.csv', index=False)
    segments.to_csv('outputs/plan_segments.csv', index=False)
    print(overall.to_string(index=False))
    print(segments.to_string(index=False))
