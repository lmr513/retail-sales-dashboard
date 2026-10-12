import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("SampleSuperstore.csv")
print("Shape:", df.shape)
print("\nMissing values:\n", df.isna().sum())
print("\nSales and profit by category:\n", df.groupby("Category")[["Sales", "Profit"]].sum())
print("\nProfit by customer segment:\n", df.groupby("Segment")["Profit"].sum().sort_values(ascending=False))
print("\nTop states by sales:\n", df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10))

summary = df.groupby("Category", as_index=False)[["Sales", "Profit"]].sum()
summary.plot(x="Category", y=["Sales", "Profit"], kind="bar", title="Sales and Profit by Category")
plt.tight_layout()
plt.savefig("category_sales_profit.png", dpi=150)
