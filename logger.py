import json
import uuid
from pathlib import Path
from datetime import datetime

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


class RunLogger:

    def __init__(self):
        self.run_id = str(uuid.uuid4())
        self.file = LOG_DIR / f"{self.run_id}.jsonl"

    def log(self, step, data=None):

        event = {
            "timestamp": datetime.utcnow().isoformat(),
            "step": step,
            "data": data
        }

        with open(self.file, "a") as f:
            f.write(json.dumps(event) + "\n")

    @property
    def filename(self):
        return self.file.name