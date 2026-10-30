"""Reproducible synthetic customer dataset; no real customer data."""
from pathlib import Path
import numpy as np
import pandas as pd


def generate(n=5000, seed=42):
    rng = np.random.default_rng(seed)
    tenure = rng.integers(1, 49, n)
    spend = np.round(rng.gamma(4, 18, n), 2)
    tickets = rng.poisson(1.1, n)
    discounts = rng.binomial(1, .35, n)
    engagement = rng.integers(0, 31, n)
    plan = rng.choice(['basic', 'standard', 'premium'], n, p=[.45, .38, .17])
    logit = (-.8 - .045 * tenure + .28 * tickets - .055 * engagement
             + .35 * discounts + .35 * (plan == 'basic') - .25 * (plan == 'premium'))
    churn = rng.binomial(1, 1 / (1 + np.exp(-logit)))
    return pd.DataFrame({'customer_id': np.arange(1, n + 1),
        'tenure_months': tenure, 'monthly_spend': spend,
        'support_tickets_90d': tickets, 'discount_user': discounts,
        'engagement_days_30d': engagement, 'plan': plan, 'churned': churn})


if __name__ == '__main__':
    path = Path('data/customers.csv')
    path.parent.mkdir(parents=True, exist_ok=True)
    generate().to_csv(path, index=False)
    print(f'Generated {path}')
