import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Retail Sales Decision Dashboard", page_icon="📊", layout="wide")

@st.cache_data
def load_data():
    data = pd.read_csv("SampleSuperstore.csv")
    for col in ["Sales", "Profit", "Quantity", "Discount"]:
        data[col] = pd.to_numeric(data[col], errors="coerce")
    return data.dropna(subset=["Sales", "Profit"])

df = load_data()
st.title("Retail Sales Decision Dashboard")
st.write("A decision-support dashboard for retail managers. Explore sales and profitability by region, product category, customer segment, state, and discount level.")
st.info("This version of SampleSuperstore.csv has 9,994 records and 13 columns, but no order-date column. Therefore, this dashboard focuses on product, geography, customer-segment, and discount analysis rather than monthly trends.")

with st.sidebar:
    st.header("Filters")
    regions = sorted(df["Region"].dropna().unique())
    categories = sorted(df["Category"].dropna().unique())
    segments = sorted(df["Segment"].dropna().unique())
    states = sorted(df["State"].dropna().unique())
    selected_regions = st.multiselect("Region", regions, default=regions)
    selected_categories = st.multiselect("Category", categories, default=categories)
    selected_segments = st.multiselect("Customer Segment", segments, default=segments)
    selected_states = st.multiselect("State", states, default=states)

data = df[
    df["Region"].isin(selected_regions)
    & df["Category"].isin(selected_categories)
    & df["Segment"].isin(selected_segments)
    & df["State"].isin(selected_states)
].copy()

if data.empty:
    st.warning("No records match the selected filters. Please adjust the filters.")
    st.stop()

sales = data["Sales"].sum()
profit = data["Profit"].sum()
margin = (profit / sales * 100) if sales else 0
a, b, c, d = st.columns(4)
a.metric("Total Sales", f"${sales:,.2f}")
b.metric("Total Profit", f"${profit:,.2f}")
c.metric("Profit Margin", f"{margin:.1f}%")
d.metric("Records", f"{len(data):,}")

left, right = st.columns(2)
with left:
    st.subheader("Sales by Category")
    chart = data.groupby("Category", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False)
    fig, ax = plt.subplots()
    ax.bar(chart["Category"], chart["Sales"])
    ax.set_ylabel("Sales ($)")
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

with right:
    st.subheader("Profit by Category")
    chart = data.groupby("Category", as_index=False)["Profit"].sum().sort_values("Profit", ascending=False)
    fig, ax = plt.subplots()
    ax.bar(chart["Category"], chart["Profit"])
    ax.set_ylabel("Profit ($)")
    ax.axhline(0, linewidth=1)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

left, right = st.columns(2)
with left:
    st.subheader("Profit by Customer Segment")
    chart = data.groupby("Segment", as_index=False)["Profit"].sum().sort_values("Profit", ascending=False)
    fig, ax = plt.subplots()
    ax.bar(chart["Segment"], chart["Profit"])
    ax.set_ylabel("Profit ($)")
    ax.axhline(0, linewidth=1)
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

with right:
    st.subheader("Top 10 States by Sales")
    chart = data.groupby("State", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False).head(10)
    chart = chart.sort_values("Sales")
    fig, ax = plt.subplots()
    ax.barh(chart["State"], chart["Sales"])
    ax.set_xlabel("Sales ($)")
    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

st.subheader("Discount vs. Profitability")
discount = data.groupby("Discount", as_index=False).agg(
    Records=("Profit", "size"), Sales=("Sales", "sum"),
    Profit=("Profit", "sum"), Average_Profit=("Profit", "mean")
).sort_values("Discount")
st.dataframe(discount, use_container_width=True, hide_index=True)

st.subheader("Sub-category Performance")
subcat = data.groupby("Sub-Category", as_index=False).agg(
    Sales=("Sales", "sum"), Profit=("Profit", "sum"), Quantity=("Quantity", "sum")
).sort_values("Profit", ascending=False)
st.dataframe(subcat, use_container_width=True, hide_index=True)

st.subheader("Filtered Data Preview")
st.dataframe(data.head(100), use_container_width=True, hide_index=True)
st.download_button("Download filtered data as CSV", data=data.to_csv(index=False).encode("utf-8"),
                   file_name="filtered_superstore_data.csv", mime="text/csv")
