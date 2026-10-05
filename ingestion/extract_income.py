import os
from dotenv import load_dotenv
import simfin as sf

load_dotenv()

api_key = os.getenv("SIMFIN_API_KEY")

if not api_key:
    raise RuntimeError("SIMFIN_API_KEY is not set")


sf.set_api_key(api_key)

sf.set_data_dir("data/simfin_cache")


income = sf.load_income(
    variant="annual",
    market="us"
)


tickers = ["NVDA", "AMD", "QCOM", "INTC"]

semiconductor_income = income[
    income.index.get_level_values(0).isin(tickers)
]


print(semiconductor_income.head())
print()
print(semiconductor_income.columns.tolist())


semiconductor_income.reset_index().to_csv(
    "data/raw/income_annual_semiconductors.csv",
    index=False
)