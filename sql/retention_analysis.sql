-- SQLite queries; import generated CSV into table customers.
SELECT COUNT(*) AS customers, ROUND(AVG(churned * 1.0), 4) AS churn_rate,
       ROUND(SUM(monthly_spend), 2) AS monthly_revenue_proxy FROM customers;

SELECT plan, COUNT(*) AS customers,
       ROUND(AVG(churned * 1.0), 4) AS churn_rate,
       ROUND(AVG(monthly_spend), 2) AS avg_monthly_spend
FROM customers GROUP BY plan ORDER BY churn_rate DESC;

SELECT CASE WHEN engagement_days_30d < 7 THEN 'low'
            WHEN engagement_days_30d < 20 THEN 'medium'
            ELSE 'high' END AS engagement_segment,
       COUNT(*) AS customers, ROUND(AVG(churned * 1.0), 4) AS churn_rate
FROM customers GROUP BY engagement_segment ORDER BY churn_rate DESC;

SELECT CASE WHEN tenure_months <= 6 THEN '0-6 months'
            WHEN tenure_months <= 18 THEN '7-18 months'
            ELSE '19+ months' END AS tenure_group,
       COUNT(*) AS customers, ROUND(AVG(churned * 1.0), 4) AS churn_rate
FROM customers GROUP BY tenure_group;
