from planner import choose_operation
from executor import execute
from tools import extract_urls, load_dataframe
from logger import RunLogger


def solve(question, history):

    logger = RunLogger()

    logger.log("received_question", question)

    urls = extract_urls(question)

    if not urls:

        logger.log("no_dataset")

        return {
            "answer": "No dataset URL found.",
            "log_file": logger.filename
        }

    logger.log("dataset_found", urls[0])

    df = load_dataframe(urls[0])

    logger.log("dataset_loaded", {"rows": len(df)})

    operation = choose_operation(question)

    logger.log("operation", operation)

    result = execute(operation, df)

    logger.log("completed")

    return {
        "answer": result,
        "log_file": logger.filename
    }