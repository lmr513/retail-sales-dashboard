# Retail Sales Decision Dashboard

## 1. Business Purpose

### Target User

The primary user is a retail store manager who monitors sales and profitability across product categories, customer segments, and geographic regions. The manager reviews the dashboard weekly to identify areas that may require further investigation.

### Business Decision

The dashboard helps the manager identify product categories or customer segments with high sales but relatively low profit. If this pattern appears, the manager can investigate discounts, product costs, and pricing before deciding whether to adjust promotional strategies.

### Why a Dashboard?

Without a dashboard, the manager may need to manually filter spreadsheets and compare sales and profit across multiple categories and regions. This dashboard brings key performance indicators and supporting comparisons together in one place, allowing the manager to investigate the same business questions regularly.

A dashboard is more useful than a one-time report when the manager needs to review performance repeatedly and interactively explore different parts of the business.

## 2. Dataset

The project uses the Sample Superstore dataset, which contains 9,994 records and 13 columns.

The dataset includes sales transactions and information about products, customers, and geographic regions. Key variables include:

- Sales and Profit
- Quantity and Discount
- Product Category and Sub-Category
- Region, State, and Customer Segment

Each row represents a recorded sales order line. The dataset is used to analyze sales performance and profitability across different business dimensions.

**Data limitation:** The CSV file used in this project does not contain an order-date column. Therefore, monthly trends and time-series analysis cannot be performed using the available data.

## 3. Dashboard Features

The dashboard includes:

- Key performance indicators: Total Sales, Total Profit, Profit Margin, and Record Count
- Sales and profit by product category
- Profit by customer segment
- Top 10 states by sales
- Discount and profitability analysis
- Sub-category performance table
- Interactive filters for exploring the data
- Filtered-data preview and CSV download

These features help the manager compare business performance across product categories, customer segments, and locations.

## 4. Business Questions

The dashboard is designed to help answer the following questions:

1. Which product categories generate the highest sales and profit?
2. Which customer segments contribute the most profit?
3. Which states have the highest sales?
4. How are discount levels associated with profitability?
5. Which product sub-categories may require further investigation because of weak profitability?

The dashboard supports investigation rather than automatically making business decisions. Managers should consider additional information before changing prices, discounts, or product strategies.

## 5. Exploratory Data Analysis and Design Choices

Before building the dashboard, the dataset was reviewed to understand its structure, variables, and potential business uses.

The dashboard prioritizes four headline metrics: Total Sales, Total Profit, Profit Margin, and Record Count. These metrics summarize overall sales activity and profitability.

Supporting charts compare sales and profit across product categories, customer segments, and states. Interactive filters allow users to investigate different regions, categories, customer segments, and states without viewing the entire dataset at once.

The dashboard does not include monthly sales trends because the available CSV file has no order-date column. It also does not include forecasting because the dataset alone does not provide sufficient time-series information for a meaningful forecast.

One important limitation is that an association between discounts and profit does not establish that discounts cause lower profit. Profitability can also be affected by product mix, costs, and other business conditions.

## 6. Review Frequency and Intended Data Refresh

The proposed dashboard is intended for weekly review by a retail store manager.

In a production environment, the data could be refreshed nightly if updated transaction data were available. The manager could review the dashboard each week and investigate categories or customer segments with high sales but weak profitability.

For example, if a category consistently shows strong sales but low or negative profit, the manager could investigate discount levels, product costs, and pricing before taking action.

The current dataset is a static CSV file, so the deployed dashboard does not automatically receive new transactions. The data period should be verified from the original dataset documentation before reporting a specific date range.

If the data becomes outdated, the manager may make decisions based on business conditions that no longer reflect current performance. A production version should display the latest data-update date.

## 7. Limitations

This project provides descriptive analysis of a sample retail dataset. Its findings should be interpreted with the following limitations in mind:

- The available CSV file has no order-date column, preventing time-series analysis.
- The dataset is static and does not automatically update with new transactions.
- The analysis identifies patterns and associations but does not establish causation.
- The results may not represent every retail business or current market conditions.
- Decisions about pricing, discounts, and product strategies should consider additional information, such as product costs and operational constraints.

## 8. Run Locally

Python and the required packages must be installed.

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start the dashboard:

```bash
streamlit run app.py
```

The terminal will display a local URL where the dashboard can be opened.

For deployment, use the Python version required by the course and supported by the selected dependencies.

## 9. Deployment

The application is deployed using Streamlit Community Cloud.

To deploy:

1. Create a public GitHub repository.
2. Upload `app.py`, `requirements.txt`, `README.md`, and `SampleSuperstore.csv`, along with any other files required by the application.
3. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) with GitHub.
4. Create an app and select the repository and branch.
5. Set the main file path to `app.py`.
6. Deploy and test the application.

**GitHub Repository:** https://github.com/lmr513/retail-sales-dashboard

**Live Dashboard:** https://retail-sales-dashboard-3uxzu47psocbb5puvmgsps.streamlit.app/
