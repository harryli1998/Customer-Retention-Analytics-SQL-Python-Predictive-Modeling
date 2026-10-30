"""Churn classification: majority-prior baseline vs logistic regression."""
from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.dummy import DummyClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, average_precision_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def evaluate(df):
    x = df.drop(columns=['customer_id', 'churned'])
    y = df['churned']
    a, b, ya, yb = train_test_split(x, y, test_size=.25, stratify=y, random_state=42)
    numeric = list(x.select_dtypes(include='number').columns)
    categorical = list(x.select_dtypes(exclude='number').columns)
    preprocessing = ColumnTransformer([
        ('numeric', Pipeline([('fill', SimpleImputer(strategy='median')),
                              ('scale', StandardScaler())]), numeric),
        ('categorical', Pipeline([('fill', SimpleImputer(strategy='most_frequent')),
                                  ('onehot', OneHotEncoder(handle_unknown='ignore'))]), categorical)])
    models = {'prior_baseline': DummyClassifier(strategy='prior'),
        'logistic_regression': Pipeline([('preprocess', preprocessing),
                                         ('classifier', LogisticRegression(max_iter=1000))])}
    results = []
    for name, model in models.items():
        model.fit(a, ya)
        p = model.predict_proba(b)[:, 1]
        results.append({'model': name, 'roc_auc': roc_auc_score(yb, p),
            'average_precision': average_precision_score(yb, p), 'test_customers': len(yb)})
    return pd.DataFrame(results)


if __name__ == '__main__':
    results = evaluate(pd.read_csv('data/customers.csv'))
    Path('outputs').mkdir(exist_ok=True)
    results.to_csv('outputs/model_metrics.csv', index=False)
    print(results.to_string(index=False))
