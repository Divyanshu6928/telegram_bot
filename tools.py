import io
import re
import requests
import pandas as pd

URL_REGEX = r"https?://[^\s]+"


def extract_urls(text: str):
    return re.findall(URL_REGEX, text)


def download_file(url: str):
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.content


def load_dataset(url: str):
    data = download_file(url)

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