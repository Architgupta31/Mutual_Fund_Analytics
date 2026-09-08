-- Query 1: Top 5 fund houses by AUM

SELECT
    fund_house,
    SUM(aum_crore) AS total_aum_crore
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum_crore DESC
LIMIT 5;
-- Query 2: Average NAV per month

SELECT
    strftime('%Y-%m', nav_date) AS month,
    ROUND(AVG(nav), 2) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;
-- Query 3: SIP inflow YoY growth

SELECT
    month,
    sip_inflow_crore,
    yoy_growth_pct
FROM fact_sip_industry
ORDER BY month;
-- Query 4: Transactions by state

SELECT
    state,
    COUNT(*) AS transaction_count,
    SUM(amount_inr) AS total_transaction_amount
FROM fact_transactions
GROUP BY state
ORDER BY transaction_count DESC;
-- Query 5: Funds with expense ratio below 1%

SELECT
    amfi_code,
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct ASC;
-- Query 6: Top 10 funds by 3-year return

SELECT
    f.scheme_name,
    f.fund_house,
    p.return_3yr_pct,
    p.sharpe_ratio,
    p.alpha
FROM fact_performance p
JOIN dim_fund f
    ON p.amfi_code = f.amfi_code
ORDER BY p.return_3yr_pct DESC
LIMIT 10;
-- Query 7: Average Sharpe ratio by fund category

SELECT
    f.category,
    ROUND(AVG(p.sharpe_ratio), 2) AS average_sharpe_ratio
FROM fact_performance p
JOIN dim_fund f
    ON p.amfi_code = f.amfi_code
GROUP BY f.category
ORDER BY average_sharpe_ratio DESC;
-- Query 8: Number of transactions by transaction type

SELECT
    transaction_type,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount_inr), 2) AS total_amount_inr
FROM fact_transactions
GROUP BY transaction_type
ORDER BY transaction_count DESC;
-- Query 9: Fund count by risk category

SELECT
    risk_category,
    COUNT(*) AS fund_count
FROM dim_fund
GROUP BY risk_category
ORDER BY fund_count DESC;
-- Query 10: Top 10 funds with highest Alpha

SELECT
    f.scheme_name,
    f.fund_house,
    p.alpha,
    p.return_3yr_pct,
    p.sharpe_ratio
FROM fact_performance p
JOIN dim_fund f
    ON p.amfi_code = f.amfi_code
ORDER BY p.alpha DESC
LIMIT 10;