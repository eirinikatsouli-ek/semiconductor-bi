import os
from dotenv import load_dotenv
import simfin as sf


load_dotenv()

api_key = os.getenv("SIMFIN_API_KEY")

if not api_key:
    raise RuntimeError("SIMFIN_API_KEY is not set")


sf.set_api_key(api_key)
sf.set_data_dir("data/simfin_cache")


TICKERS = ["NVDA", "AMD", "QCOM", "INTC"]


def filter_companies(df):
    return df[
        df.index.get_level_values(0).isin(TICKERS)
    ]


# Income Statement
income = sf.load_income(
    variant="annual",
    market="us"
)

income_filtered = filter_companies(income)

income_filtered.reset_index().to_csv(
    "data/raw/income_annual_semiconductors.csv",
    index=False
)


# Balance Sheet
balance = sf.load_balance(
    variant="annual",
    market="us"
)

balance_filtered = filter_companies(balance)

balance_filtered.reset_index().to_csv(
    "data/raw/balance_annual_semiconductors.csv",
    index=False
)


# Cash Flow Statement
cashflow = sf.load_cashflow(
    variant="annual",
    market="us"
)

cashflow_filtered = filter_companies(cashflow)

cashflow_filtered.reset_index().to_csv(
    "data/raw/cashflow_annual_semiconductors.csv",
    index=False
)


print("Extraction completed.")

print("Income:", income_filtered.shape)
print("Balance:", balance_filtered.shape)
print("Cash Flow:", cashflow_filtered.shape)