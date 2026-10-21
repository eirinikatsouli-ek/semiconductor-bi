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

print(type(income))
print(income.shape)
print(income.head())
print(income.index.names)
