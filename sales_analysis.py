import pandas as pd

df = pd.read_csv('sales_data.csv')

print(df.head())

print("\nShape of data:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nBasic info:")
print(df.info())

print("\nMissing values in each column:")
print(df.isnull().sum())

df = df.dropna()

df = df.drop_duplicates()

total_sales = df['Total_Sales'].sum()
print(f"\nTotal Sales: ₹{total_sales}")

best_product = df.groupby('Product')['Total_Sales'].sum().idxmax()
print(f"Best Selling Product: {best_product}")

average_sales = df['Total_Sales'].mean()
print(f"Average Sales: ₹{average_sales}")

max_sales = df['Total_Sales'].max()
min_sales = df['Total_Sales'].min()

print(f"Highest Sale: ₹{max_sales}")
print(f"Lowest Sale: ₹{min_sales}")
