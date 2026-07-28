import io
import re
import requests
import pandas as pd

URL_PATTERN = r"https?://[^\s]+"


def extract_urls(text: str):
    return re.findall(URL_PATTERN, text)


def download(url: str):
    r = requests.get(url, timeout=60)
    r.raise_for_status()
    return r.content


def load_dataframe(url: str):

    content = download(url)

    url = url.lower()

    if url.endswith(".csv"):
        return pd.read_csv(io.BytesIO(content))

    if url.endswith(".xlsx") or url.endswith(".xls"):
        return pd.read_excel(io.BytesIO(content))

    if url.endswith(".json"):
        return pd.read_json(io.BytesIO(content))

    try:
        tables = pd.read_html(io.BytesIO(content))
        if tables:
            return tables[0]
    except:
        pass

    raise Exception("Unsupported dataset")