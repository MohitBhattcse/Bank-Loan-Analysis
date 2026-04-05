📊 Bank Loan Analysis Report
📌 Project Overview
This project performs an end‑to‑end exploratory data analysis (EDA) and visualization on bank loan data using Python.
The objective is to analyze loan performance, customer behavior, funding trends, and risk metrics to support data‑driven decision‑making.
The analysis computes key KPIs, compares good vs bad loans, and visualizes trends across time, geography, loan terms, employment length, loan purpose, and home ownership.

🎯 Objectives

Understand overall loan portfolio performance
Analyze funded vs received amounts
Track monthly trends
Compare good loans vs bad loans
Identify patterns across:

States
Loan terms
Employment length
Loan purpose
Home ownership type




📂 Dataset Used

File: financial_loan.xlsx
Key columns:

id
issue_date
application_type
emp_length
grade
annual_income
loan_amount
total_payment
loan_status
int_rate
dti
term
emp_length
purpose
address_state
home_ownership
installment
verification_status
sub_grade
next_payment_date
last_payment_date
last_credit_pull_date




🛠️ Tools & Libraries

Python
NumPy
Pandas
Matplotlib
Seaborn
Plotly Express


📈 Key Metrics Calculated
🔹 Portfolio KPIs

Total Loan Applications
Total Funded Amount
Total Amount Received
Average Interest Rate
Average Debt‑to‑Income (DTI) Ratio

🔹 Month‑to‑Date (MTD) Metrics

Current Month Applications
Current Month Funded Amount
Current Month Amount Received


✅ Good vs Bad Loan Analysis
🟢 Good Loans

Status: Fully Paid / Current
Metrics:

Number of applications
Percentage share
Total funded amount
Total received amount



🔴 Bad Loans

Status: Charged Off
Metrics:

Number of applications
Percentage share
Total funded amount
Total received amount




📊 Visualizations & Insights
📅 Monthly Trends

Total Funded Amount by Month
Total Received Amount by Month
Total Loan Applications by Month
(Area + line plots with data labels)

🌍 Regional Analysis (State‑wise)

Funded Amount
Received Amount
Total Applications
(Horizontal bar charts)

⏳ Loan Term Analysis

Funded Amount by Term (Donut chart)
Received Amount by Term (Donut chart)
Applications by Term (Donut chart)

👨‍💼 Employment Length Analysis

Funded Amount
Received Amount
Total Applications
(Horizontal bar charts)

🎯 Loan Purpose Analysis

Funded Amount (₹ Millions)
Received Amount (₹ Millions)
Total Applications
(Horizontal bar charts)

🏠 Home Ownership Analysis (Treemap)

Funded Amount
Received Amount
Total Applications
(Interactive Plotly Treemaps)


🧠 Key Insights

Monthly loan funding shows clear seasonal trends
Longer employment length correlates with higher funded and received amounts
Certain loan purposes dominate both funding and application volumes
Home ownership type strongly influences loan distribution
Good loans form the majority of the portfolio, indicating healthy repayment behavior


📌 Why Treemaps Were Used
Treemaps effectively represent proportional distribution and allow easy comparison across categories, especially for:

Home ownership analysis
Hierarchical financial breakdowns


✅ Project Highlights

Clean data transformation using Pandas
Advanced KPI calculations
Interactive Plotly visualizations
Dashboard‑ready charts
Interview‑friendly business logic
