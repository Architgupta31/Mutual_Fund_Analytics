# Bluestock Mutual Fund Analytics
## Data Dictionary

This document describes the datasets, columns, data types, business meanings, and data sources used in the Mutual Fund Analytics project.

---

# 1. fund_master.csv

| Column | Data Type | Business Definition | Source |
|---|---|---|---|
| amfi_code | TEXT | Unique AMFI scheme code | AMFI India |
| fund_house | TEXT | Name of the mutual fund house / AMC | AMFI India |
| scheme_name | TEXT | Full mutual fund scheme name | AMFI India |
| category | TEXT | Main fund category such as Equity or Debt | AMFI India |
| sub_category | TEXT | Detailed fund category such as Large Cap, Mid Cap, Small Cap, Liquid | AMFI India |
| plan | TEXT | Fund plan, such as Regular or Direct | AMFI India |
| launch_date | DATE | Date on which the fund was launched | AMFI India |
| benchmark | TEXT | Benchmark index associated with the fund | AMFI India |
| expense_ratio_pct | REAL | Annual expense ratio in percentage | AMFI India |
| exit_load_pct | REAL | Exit load charged on applicable redemptions | AMFI India |
| min_sip_amount | REAL | Minimum amount required for SIP investment | AMFI India |
| min_lumpsum_amount | REAL | Minimum amount required for lumpsum investment | AMFI India |
| fund_manager | TEXT | Primary fund manager of the scheme | AMFI India |
| risk_category | TEXT | SEBI risk category of the fund | AMFI India |
| sebi_category_code | TEXT | Internal SEBI category code | AMFI India |

---

# 2. nav_history.csv

| Column | Data Type | Business Definition | Source |
|---|---|---|---|
| amfi_code | TEXT | AMFI scheme code | AMFI India / mfapi.in |
| date | DATE | NAV date | mfapi.in |
| nav | REAL | Net Asset Value of the mutual fund in INR | mfapi.in |

---

# 3. aum_by_fund_house.csv

| Column | Data Type | Business Definition | Source |
|---|---|---|---|
| date | DATE | AUM reporting date | AMFI India |
| fund_house | TEXT | Mutual fund house / AMC | AMFI India |
| aum_lakh_crore | REAL | Assets under management measured in lakh crore | AMFI India |
| aum_crore | REAL | Assets under management measured in crore | AMFI India |
| num_schemes | INTEGER | Number of schemes managed by the fund house | AMFI India |

---

# 4. monthly_sip_inflows.csv

| Column | Data Type | Business Definition | Source |
|---|---|---|---|
| month | TEXT | Month in YYYY-MM format | AMFI India |
| sip_inflow_crore | REAL | Total monthly SIP inflow in crore INR | AMFI India |
| active_sip_accounts_crore | REAL | Number of active SIP accounts in crore | AMFI India |
| new_sip_accounts_lakh | REAL | New SIP registrations in lakh accounts | AMFI India |
| sip_aum_lakh_crore | REAL | SIP assets under management in lakh crore | AMFI India |
| yoy_growth_pct | REAL | Year-over-year growth percentage in SIP inflows | Computed from AMFI data |

---

# 5. category_inflows.csv

| Column | Data Type | Business Definition | Source |
|---|---|---|---|
| month | DATE | Reporting month | AMFI India |
| category | TEXT | Mutual fund category | AMFI India |
| net_inflow_crore | REAL | Net inflow into the fund category in crore INR | AMFI India |

---

# 6. industry_folio_count.csv

| Column | Data Type | Business Definition | Source |
|---|---|---|---|
| month | DATE | Reporting month | AMFI India |
| total_folios_crore | REAL | Total mutual fund folios in crore | AMFI India |
| equity_folios_crore | REAL | Equity mutual fund folios in crore | AMFI India |
| debt_folios_crore | REAL | Debt mutual fund folios in crore | AMFI India |
| hybrid_folios_crore | REAL | Hybrid mutual fund folios in crore | AMFI India |
| others_folios_crore | REAL | Other mutual fund folios in crore | AMFI India |

---

# 7. scheme_performance.csv

| Column | Data Type | Business Definition | Source |
|---|---|---|---|
| amfi_code | TEXT | AMFI scheme code | AMFI India |
| return_1yr_pct | REAL | One-year absolute return percentage | Computed / dataset |
| return_3yr_pct | REAL | Three-year CAGR percentage | Computed / dataset |
| return_5yr_pct | REAL | Five-year CAGR percentage | Computed / dataset |
| benchmark_3yr_pct | REAL | Three-year benchmark CAGR percentage | Benchmark data |
| alpha | REAL | Return above benchmark | Computed |
| beta | REAL | Sensitivity of fund returns to market returns | Computed |
| sharpe_ratio | REAL | Risk-adjusted return measure | Computed |
| sortino_ratio | REAL | Risk-adjusted return using downside volatility | Computed |
| std_dev_ann_pct | REAL | Annualised standard deviation of daily returns | Computed |
| max_drawdown_pct | REAL | Maximum peak-to-trough decline | Computed |
| expense_ratio_pct | REAL | Annual expense ratio percentage | AMFI India |
| morningstar_rating | INTEGER | Fund rating from 1 to 5 | Dataset |

---

# 8. investor_transactions.csv

| Column | Data Type | Business Definition | Source |
|---|---|---|---|
| investor_id | TEXT | Unique investor identifier | Synthetic dataset |
| transaction_date | DATE | Date of transaction | Synthetic dataset |
| amfi_code | TEXT | Fund involved in the transaction | AMFI India |
| transaction_type | TEXT | SIP, Lumpsum, or Redemption | Synthetic dataset |
| amount_inr | REAL | Transaction amount in Indian Rupees | Synthetic dataset |
| state | TEXT | Investor state | Synthetic dataset |
| city | TEXT | Investor city | Synthetic dataset |
| city_tier | TEXT | T30 or B30 city classification | Synthetic dataset / AMFI classification |
| age_group | TEXT | Investor age group | Synthetic dataset |
| gender | TEXT | Investor gender | Synthetic dataset |
| annual_income_lakh | REAL | Annual investor income in lakh INR | Synthetic dataset |
| payment_mode | TEXT | Payment method such as UPI, Net Banking, Mandate, or Cheque | Synthetic dataset |
| kyc_status | TEXT | KYC verification status | Synthetic dataset |

---

# 9. portfolio_holdings.csv

| Column | Data Type | Business Definition | Source |
|---|---|---|---|
| amfi_code | TEXT | AMFI scheme code | AMFI India |
| stock_symbol | TEXT | Stock exchange symbol of the holding | Portfolio dataset |
| stock_name | TEXT | Name of the stock held by the fund | Portfolio dataset |
| sector | TEXT | Industry sector of the holding | Portfolio dataset |
| weight_pct | REAL | Percentage weight of the holding in the portfolio | Portfolio dataset |
| market_value_cr | REAL | Market value of the holding in crore INR | Portfolio dataset |
| current_price_inr | REAL | Current stock price in INR | Market data |
| portfolio_date | DATE | Portfolio reporting date | Portfolio dataset |

---

# 10. benchmark_indices.csv

| Column | Data Type | Business Definition | Source |
|---|---|---|---|
| date | DATE | Benchmark index date | NSE / BSE |
| index_name | TEXT | Name of the benchmark index | NSE / BSE |
| close_value | REAL | Closing value of the benchmark index | NSE / BSE |

---

# Data Sources

The project uses publicly available financial data.

- AMFI India: Mutual fund NAV, AUM, folio and SIP information
- mfapi.in: Historical mutual fund NAV data
- NSE India: Benchmark index prices
- BSE India: Benchmark index prices
- AMFI Monthly Notes: Industry SIP and flow data

Investor transaction data is synthetically generated for educational and analytical purposes.

---

# Data Quality Notes

- NAV dates are converted to date format during cleaning.
- Duplicate records are checked and removed where required.
- NAV values are validated to be greater than zero.
- Transaction amounts are validated to be greater than zero.
- Transaction types are standardised to SIP, Lumpsum and Redemption.
- Performance fields are converted to numeric values.
- Expense ratios are checked against the expected 0.1% to 2.5% range.
- Missing SIP YoY growth values are retained where prior-year data is unavailable.
