import json
import os
from datetime import datetime

LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)


def create_log():

    filename = datetime.now().strftime("%Y%m%d_%H%M%S.jsonl")

    path = os.path.join(LOG_DIR, filename)

    return path


def log(path, event):

    with open(path, "a", encoding="utf8") as f:
        f.write(json.dumps(event) + "\n")