import pandas as pd

FILE_PATH = "data/raw/income_annual_semiconductors.csv"

df = pd.read_csv(FILE_PATH)

print("\n--- dataset shape ---")
print(df.shape)

print("\n--- columns ---")
print(df.columns.tolist())

print("\n--- companies ---")
print(df["Ticker"].value_counts().sort_index())

print("\n--- fiscal year range by company ---")
print(
    df.groupby("Ticker")["Fiscal Year"]
    .agg(["min", "max", "count"])
)

print("\n--- duplicates: ticker + fiscal year ---")
duplicates = df.duplicated(
    subset=["Ticker", "Fiscal Year"],
    keep=False
)

print(df[duplicates][["Ticker", "Fiscal Year", "Report Date"]])

print("\n--- missing values ---")
missing = df.isna().sum()
print(missing[missing > 0].sort_values(ascending=False))