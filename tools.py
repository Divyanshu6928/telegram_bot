import io
import re
import requests
import pandas as pd

URL_PATTERN = r"https?://[^\s]+"

def extract_urls(text):
    return re.findall(URL_PATTERN, text)

def load_dataframe(url):
    response = requests.get(url, timeout=60)
    response.raise_for_status()

    data = response.content
    lower = url.lower()

    if lower.endswith(".csv"):
        return pd.read_csv(io.BytesIO(data))

    if lower.endswith(".xlsx") or lower.endswith(".xls"):
        return pd.read_excel(io.BytesIO(data))

    if lower.endswith(".json"):
        return pd.read_json(io.BytesIO(data))

    try:
        tables = pd.read_html(io.BytesIO(data))
        if tables:
            return tables[0]
    except Exception:
        pass

    raise Exception("Unsupported dataset")