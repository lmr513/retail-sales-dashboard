# Retail Sales Decision Dashboard

## 1. Project Overview

The Retail Sales Decision Dashboard is an interactive data application built with Python, Pandas, Matplotlib, and Streamlit. It helps retail managers monitor sales performance, understand profitability, and identify areas that may require further investigation.

**Target User:** Retail managers

**Business Goal:** Support decisions about product performance, discount policies, and regional sales by making sales and profitability patterns easier to explore.

## 2. Dataset

**Dataset Name:** Sample Superstore

**Source:** [Sample Superstore Dataset — Kaggle](https://www.kaggle.com/datasets/xubao666/superstore)

The dataset contains historical retail order records, including order dates, shipping dates, sales, profit, quantity, discounts, product categories, customer segments, and geographic information.

The data is a historical snapshot rather than a live feed. Therefore, the dashboard describes the available historical records and does not automatically reflect new transactions.

## 3. Why a Dashboard?

Retail managers need to review sales and profitability regularly and investigate unexpected changes. A dashboard brings key metrics, trends, and comparisons into one place.

Compared with a static report or weekly email, an interactive dashboard allows users to filter by date, region, category, customer segment, and state. Managers can investigate a result without manually preparing a new report for each question.

## 4. Key Metrics and Visualizations

### Headline Metrics

- **Total Sales:** Shows the sales value of the selected records.
- **Total Profit:** Shows the combined profit or loss.
- **Profit Margin:** Measures profit as a percentage of sales.
- **Record Count:** Shows how many records are included in the current selection.

Sales and profit are shown together because high sales do not necessarily mean high profitability.

### Supporting Visualizations

- **Monthly Sales Trend:** Helps identify changes in sales over time.
- **Sales and Profit by Category:** Compares product categories and highlights differences between sales and profitability.
- **Profit by Customer Segment:** Helps compare profitability across customer groups.
- **Top States by Sales:** Identifies geographic areas with high sales.
- **Discount Analysis:** Helps investigate how discount levels relate to profitability.
- **Sub-Category Summary:** Allows users to examine sales, profit, and quantity at a more detailed product level.

### Interactive Filters

Users can filter records by order date range, region, category, customer segment, and state. These filters allow managers to focus on a specific period or business area.

## 5. Design Choices and Trade-Offs

The dashboard prioritizes headline metrics and a small set of business-focused charts instead of displaying every possible analysis at once.

Individual transaction records are available in the data preview, but they are not the main focus because showing every record first would make overall patterns harder to identify.

The dashboard also avoids adding many unrelated visualizations. The selected charts focus on sales trends, profitability, customer segments, and geographic differences, which are more directly relevant to the target user's decisions.

## 6. Potential Misinterpretations and Data Limitations

The dataset is historical, so its patterns may not represent current business conditions.

Sales alone can be misleading. A category may generate substantial revenue while producing low or negative profit, so managers should consider sales and profitability together.

Discounts may be associated with lower profits, but this relationship does not prove that discounts caused the change. Product mix, order characteristics, and other factors may also influence profitability.

Unusual transactions, missing values, or invalid dates may affect the analysis. The application converts relevant numeric fields, parses order dates, and excludes records without usable sales, profit, or order-date values from the main analysis.

Business decisions should be based on further investigation rather than on a single chart or metric.

## 7. Refresh Frequency and Decision Rules

**Proposed production refresh frequency:** Nightly.

**Proposed review frequency:** Weekly, with additional investigation when unusual results appear.

The current application uses a static CSV file and does not automatically receive new transactions. A production version would require a scheduled data update and a visible indication of the latest successful refresh.

**Metric to monitor:** Profit margin.

**Proposed investigation threshold:** If profit margin falls below 10%, or decreases by at least 5 percentage points compared with the preceding comparable period, the manager should investigate the categories, regions, and discount levels associated with the change.

These thresholds are proposed examples for the assignment, not verified company policies. They should be adjusted to reflect the business's actual targets.

Stale data could cause managers to overlook recent losses or make decisions based on outdated patterns.

## 8. Technology Stack

- Python
- Pandas
- Matplotlib
- Streamlit

## 9. Project Structure

```text
retail-sales-dashboard/
├── app.py
├── eda.py
├── SampleSuperstore.csv
├── requirements.txt
├── README.md
└── START_HERE.txt
```

## 10. How to Run the Application

Install the required packages:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
streamlit run app.py
```

## 11. Deployment and Links

**Live Dashboard:** https://retail-sales-dashboard-3uxzu47psocbb5puvmgsps.streamlit.app/

**GitHub Repository:** https://github.com/lmr513/retail-sales-dashboard
