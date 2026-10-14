# Retail Sales Decision Dashboard

## Project Overview

The Retail Sales Decision Dashboard is an interactive business intelligence application built with Python, Pandas, Matplotlib, and Streamlit. It helps retail managers explore sales performance, profitability, product categories, customer segments, and regional differences.

The dashboard uses the Sample Superstore dataset and provides interactive filters to support data-driven business decisions.

## Project Objectives

- Monitor overall sales and profit performance.
- Compare sales and profitability across product categories.
- Identify differences in profitability between customer segments.
- Explore regional sales performance.
- Examine monthly sales trends over time.
- Investigate the relationship between discounts and profitability.

## Dashboard Features

- **Key Performance Indicators:** Total sales, total profit, profit margin, and number of records.
- **Order Date Filter:** Select a date range to analyze a specific period.
- **Interactive Filters:** Filter results by region, product category, customer segment, and state.
- **Monthly Sales Trend:** Examine how sales change over time.
- **Category Analysis:** Compare sales and profit across product categories.
- **Segment Analysis:** Compare profitability across customer segments.
- **Regional Analysis:** Identify states with the highest sales.
- **Discount Analysis:** Compare sales and profitability at different discount levels.
- **Sub-Category Analysis:** Review sales, profit, and quantity by product sub-category.
- **Data Preview and Export:** View filtered records and download them as a CSV file.

## Dataset

The project uses `SampleSuperstore.csv`, which contains retail transaction information.

Important fields include:

- Order Date and Ship Date
- Sales, Profit, Quantity, and Discount
- Category and Sub-Category
- Region, State, and City
- Segment and Ship Mode

The dashboard uses Order Date to filter records and generate the monthly sales trend. Results change according to the selected filters.

## Technology Stack

- Python
- Pandas
- Matplotlib
- Streamlit

## Project Structure

```text
retail-sales-dashboard/
├── app.py
├── eda.py
├── SampleSuperstore.csv
├── requirements.txt
├── README.md
└── START_HERE.txt
```

## Run Locally

1. Clone or download this repository.
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Start the dashboard:

   ```bash
   streamlit run app.py
   ```

4. Open the local URL provided by Streamlit.

## Exploratory Data Analysis

Run the following command to inspect the dataset and generate analysis outputs:

```bash
python eda.py
```

The script checks data quality, summarizes key business metrics, and saves charts in the project directory.

## Business Questions

This dashboard helps answer questions such as:

1. How do total sales and profit change over time?
2. Which product categories generate the most sales and profit?
3. Which customer segments contribute the most profit?
4. Which states have the highest sales?
5. How do discounts relate to profitability?
6. Which sub-categories have strong sales but weak or negative profit?

## Limitations

- The analysis depends on the records available in the supplied dataset.
- Historical results do not necessarily represent future performance.
- Observed relationships between discounts and profit do not, by themselves, establish causation.
- Business recommendations should consider additional factors such as operating costs, inventory, and customer behavior.

## Deployment

The application can be deployed using Streamlit Community Cloud by connecting the GitHub repository and selecting `app.py` as the application entry point.
