
from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


DATA_FILE = Path("SampleSuperstore.csv")
OUTPUT_DIR = Path("eda_outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def load_data():
    """Load the dataset and prepare the main analysis columns."""
    if not DATA_FILE.exists():
        raise FileNotFoundError(
            f"Cannot find {DATA_FILE}. "
            "Place it in the same directory as eda.py."
        )

    df = pd.read_csv(DATA_FILE, encoding="cp1252")

    required_columns = [
        "Sales",
        "Profit",
        "Quantity",
        "Discount",
        "Order Date",
        "Ship Date",
        "Category",
        "Sub-Category",
        "Segment",
        "Region",
        "State",
    ]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            "The dataset is missing required columns: "
            + ", ".join(missing_columns)
        )

    for column in ["Sales", "Profit", "Quantity", "Discount"]:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    for column in ["Order Date", "Ship Date"]:
        df[column] = pd.to_datetime(
            df[column], format="mixed", errors="coerce"
        )

    return df


def save_chart(filename):
    """Save the current Matplotlib figure."""
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / filename, dpi=150, bbox_inches="tight")
    plt.close()


def main():
    df = load_data()

    print("=" * 60)
    print("RETAIL SALES DATA EXPLORATORY ANALYSIS")
    print("=" * 60)

    # 1. Dataset overview
    print("\n1. DATASET OVERVIEW")
    print(f"Rows: {df.shape[0]:,}")
    print(f"Columns: {df.shape[1]:,}")
    print("\nColumn data types:")
    print(df.dtypes)

    # 2. Data quality
    print("\n2. DATA QUALITY CHECK")
    missing = df.isna().sum()
    missing_report = pd.DataFrame({
        "Missing Count": missing,
        "Missing Percentage": (missing / len(df) * 100).round(2),
    })
    print(missing_report.to_string())

    print(f"\nDuplicate rows: {df.duplicated().sum():,}")
    print(f"Invalid Order Dates: {df['Order Date'].isna().sum():,}")
    print(f"Invalid Ship Dates: {df['Ship Date'].isna().sum():,}")

    # 3. Date coverage
    print("\n3. DATE COVERAGE")
    print(f"Earliest order: {df['Order Date'].min()}")
    print(f"Latest order: {df['Order Date'].max()}")
    print(f"Earliest shipment: {df['Ship Date'].min()}")
    print(f"Latest shipment: {df['Ship Date'].max()}")

    # 4. Overall business metrics
    print("\n4. OVERALL BUSINESS METRICS")
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_quantity = df["Quantity"].sum()
    profit_margin = (
        total_profit / total_sales * 100
        if total_sales != 0 else 0
    )

    print(f"Total Sales: ${total_sales:,.2f}")
    print(f"Total Profit: ${total_profit:,.2f}")
    print(f"Total Quantity: {total_quantity:,.0f}")
    print(f"Overall Profit Margin: {profit_margin:.2f}%")

    print("\nNumerical summary:")
    print(
        df[["Sales", "Profit", "Quantity", "Discount"]]
        .describe()
        .round(2)
    )

    # 5. Category performance
    category_summary = (
        df.groupby("Category", as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum"),
        )
        .sort_values("Sales", ascending=False)
    )

    print("\n5. SALES AND PROFIT BY CATEGORY")
    print(category_summary.round(2).to_string(index=False))
    category_summary.to_csv(
        OUTPUT_DIR / "category_summary.csv", index=False
    )

    category_summary.plot(
        x="Category",
        y=["Sales", "Profit"],
        kind="bar",
        title="Sales and Profit by Category",
    )
    plt.ylabel("Amount")
    plt.xticks(rotation=0)
    save_chart("category_sales_profit.png")

    # 6. Customer segment performance
    segment_summary = (
        df.groupby("Segment", as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum"),
        )
        .sort_values("Profit", ascending=False)
    )

    print("\n6. PERFORMANCE BY CUSTOMER SEGMENT")
    print(segment_summary.round(2).to_string(index=False))
    segment_summary.to_csv(
        OUTPUT_DIR / "segment_summary.csv", index=False
    )

    segment_summary.plot(
        x="Segment",
        y="Profit",
        kind="bar",
        legend=False,
        title="Profit by Customer Segment",
    )
    plt.ylabel("Profit")
    plt.xticks(rotation=0)
    save_chart("segment_profit.png")

    # 7. Regional and state performance
    state_summary = (
        df.groupby("State", as_index=False)
        .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))
        .sort_values("Sales", ascending=False)
    )

    print("\n7. TOP 10 STATES BY SALES")
    print(state_summary.head(10).round(2).to_string(index=False))
    state_summary.to_csv(
        OUTPUT_DIR / "state_summary.csv", index=False
    )

    top_states = state_summary.head(10).sort_values("Sales")
    top_states.plot(
        x="State",
        y="Sales",
        kind="barh",
        legend=False,
        title="Top 10 States by Sales",
    )
    plt.xlabel("Sales")
    save_chart("top_10_states_sales.png")

    # 8. Discount and profitability
    discount_summary = (
        df.groupby("Discount", as_index=False)
        .agg(
            Orders=("Discount", "size"),
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Average_Profit=("Profit", "mean"),
        )
        .sort_values("Discount")
    )

    print("\n8. DISCOUNT AND PROFITABILITY")
    print(discount_summary.round(2).to_string(index=False))
    discount_summary.to_csv(
        OUTPUT_DIR / "discount_summary.csv", index=False
    )

    discount_summary.plot(
        x="Discount",
        y="Average_Profit",
        kind="line",
        marker="o",
        legend=False,
        title="Average Profit by Discount Level",
    )
    plt.xlabel("Discount")
    plt.ylabel("Average Profit per Record")
    save_chart("discount_average_profit.png")

    # 9. Monthly sales and profit trends
    dated_df = df.dropna(subset=["Order Date"]).copy()
    dated_df = dated_df.set_index("Order Date").sort_index()

    monthly_summary = (
        dated_df[["Sales", "Profit"]]
        .resample("MS")
        .sum()
        .reset_index()
    )

    print("\n9. MONTHLY SALES AND PROFIT")
    print(monthly_summary.head(12).round(2).to_string(index=False))
    monthly_summary.to_csv(
        OUTPUT_DIR / "monthly_summary.csv", index=False
    )

    monthly_summary.plot(
        x="Order Date",
        y="Sales",
        kind="line",
        marker="o",
        legend=False,
        title="Monthly Sales Trend",
    )
    plt.xlabel("Order Date")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    save_chart("monthly_sales_trend.png")

    monthly_summary.plot(
        x="Order Date",
        y="Profit",
        kind="line",
        marker="o",
        legend=False,
        title="Monthly Profit Trend",
    )
    plt.xlabel("Order Date")
    plt.ylabel("Profit")
    plt.xticks(rotation=45)
    save_chart("monthly_profit_trend.png")

    # 10. Sub-category performance
    subcategory_summary = (
        df.groupby("Sub-Category", as_index=False)
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum"),
        )
        .sort_values("Profit")
    )

    print("\n10. SUB-CATEGORIES WITH THE LOWEST PROFIT")
    print(subcategory_summary.head(10).round(2).to_string(index=False))
    subcategory_summary.to_csv(
        OUTPUT_DIR / "subcategory_summary.csv", index=False
    )

    subcategory_summary.head(10).sort_values("Profit").plot(
        x="Sub-Category",
        y="Profit",
        kind="barh",
        legend=False,
        title="10 Lowest-Profit Sub-Categories",
    )
    plt.xlabel("Profit")
    save_chart("lowest_profit_subcategories.png")

    print(f"\nAnalysis complete. Outputs saved to: {OUTPUT_DIR.resolve()}")


if __name__ == "__main__":
    main()
