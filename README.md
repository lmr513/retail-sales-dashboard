# Retail Sales Decision Dashboard

## 1. Business Purpose

This interactive dashboard helps retail managers evaluate sales performance and profitability. Users can filter data by region, product category, customer segment, and state to support data-driven business decisions.

## 2. Dataset

The project uses the Sample Superstore dataset, which contains 9,994 records and 13 columns.

Key variables include:
- Sales and Profit
- Quantity and Discount
- Product Category and Sub-Category
- Region, State, and Customer Segment

**Data limitation:** This version of the dataset does not contain an order-date column. Therefore, monthly and time-series analysis cannot be performed.

## 3. Dashboard Features

- Key performance indicators: Total Sales, Total Profit, Profit Margin, and Record Count
- Sales and profit by product category
- Profit by customer segment
- Top 10 states by sales
- Discount and profitability analysis
- Sub-category performance table
- Interactive filters and filtered-data preview
- CSV download of filtered records

## 4. Business Questions

- Which product categories generate the highest sales and profit?
- Which customer segments contribute most to total profit?
- Which states have the highest sales?
- How are discount levels associated with profitability?

## 5. Run Locally

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

Use a Python version supported by all project dependencies and the deployment platform. Check the course's Python 3.14 requirement before submission.

## 6. Deployment

The application is deployed using Streamlit Community Cloud.

To deploy:
1. Create a public GitHub repository.
2. Upload `app.py`, `requirements.txt`, `README.md`, and `SampleSuperstore.csv`.
3. Sign in to [Streamlit Community Cloud](https://share.streamlit.io/) with GitHub.
4. Create an app and select the repository and branch.
5. Set the main file path to `app.py`.
6. Deploy and test the application.

## 7. Limitations

This project provides descriptive analysis of a sample retail dataset. Observed associations between discounts and profitability do not establish causation. Business decisions should consider other factors, including product mix and sales conditions.
