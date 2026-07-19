import pandas as pd

files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv"
]

dfs = []

for file in files:
    df = pd.read_csv(file)

    # Keep only Pink Morsels
    df = df[df["product"].str.lower() == "pink morsel"]

    # Remove '$' and convert price to float
    df["price"] = df["price"].replace(r'[\$,]', '', regex=True).astype(float)

    # Calculate sales
    df["sales"] = df["quantity"] * df["price"]

    # Keep only required columns
    df = df[["sales", "date", "region"]]

    dfs.append(df)

# Combine all files
final_df = pd.concat(dfs, ignore_index=True)

# Save the output
final_df.to_csv("formatted_output.csv", index=False)

print(final_df.head())
print(f"\nTotal rows: {len(final_df)}")
print("\nformatted_output.csv created successfully!")