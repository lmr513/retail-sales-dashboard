# Retail Sales Decision Dashboard

## Business purpose
This dashboard helps retail managers explore sales and profitability by product category, region, state, customer segment, and discount level.

## Dataset
`SampleSuperstore.csv` contains 9,994 records and 13 columns. This version does not contain an order-date column, so monthly trends are not available.

## Run locally
Install Python and run:

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud
1. Create a **public** GitHub repository.
2. Upload `app.py`, `requirements.txt`, `README.md`, and `SampleSuperstore.csv` to the repository root.
3. Open https://share.streamlit.io/ and sign in with GitHub.
4. Choose **Create app**, select your repository and branch, and set the main file path to `app.py`.
5. Deploy and test the app.
6. Submit both the GitHub repository URL and the deployed Streamlit app URL.

## Suggested business questions
- Which product categories generate the most sales and profit?
- Which customer segments contribute most to profit?
- Which states have the highest sales?
- How do discount levels relate to profitability?

## Limitation
This is descriptive analysis of a sample dataset. Relationships between discounts and profit should not be interpreted as proof of causation.
