# Semiconductor BI

Python scripts for extracting SimFin annual income statements and profiling a semiconductor dataset.

## Setup on another computer

Install Git and Python 3.11 or newer. In PowerShell:

```powershell
git clone https://github.com/eirinikatsouli-ek/semiconductor-bi.git
cd semiconductor-bi
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Set `SIMFIN_API_KEY` in your local `.env` to your own SimFin API key. The file is ignored by Git and hidden in the VS Code Explorer. To edit it in VS Code, run `code .env` from the terminal.

Run these commands from the project root:

```powershell
# Profile the semiconductor CSV included in this repository.
.\.venv\Scripts\python.exe profiling/profile_income.py

# Download/cache annual US income statements from SimFin (requires the API key).
.\.venv\Scripts\python.exe ingestion/extract_income.py
```

The extraction script prints the downloaded dataset; it does not regenerate `data/raw/income_annual_semiconductors.csv`.

## Files in Git

Source code, the semiconductor CSV, dependency versions, editor settings and `.env.example` are versioned. Keep `.env.example` free of credentials. The local `.env`, virtual environment, Python cache, SimFin cache and processed data are excluded.

To continue work on another computer after pushing changes, run `git pull` there and reinstall dependencies if `requirements.txt` changed. Each computer needs its own local `.env`.
