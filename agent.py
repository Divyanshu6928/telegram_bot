import json
from tools import extract_urls, load_dataframe
from logger import RunLogger


class Agent:

    def __init__(self):
        self.logger = RunLogger()

    def solve(self, question: str):

        self.logger.log("question", question)

        urls = extract_urls(question)

        if not urls:
            self.logger.log("error", "No dataset URL found")

            return {
                "answer": "No dataset URL found in the message.",
                "log_file": self.logger.filename
            }

        url = urls[0]

        self.logger.log("dataset_url", url)

        df = load_dataframe(url)

        self.logger.log(
            "dataset_loaded",
            {
                "rows": len(df),
                "columns": list(df.columns)
            }
        )

        answer = {
            "rows": len(df),
            "columns": list(df.columns),
            "shape": list(df.shape)
        }

        self.logger.log("completed")

        return {
            "answer": answer,
            "log_file": self.logger.filename
        }