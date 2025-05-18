import json
import logging

def get_logger():
    """Get logger.
        Get same name logger and set format and so on.

    """
    logger = logging.getLogger("logger")
    if logger.hasHandlers():
        return logger
    st_handler = logging.StreamHandler()
    format = "[%(levelname)s] %(message)s"
    st_handler.setFormatter(logging.Formatter(format))
    logger.setLevel(logging.INFO)
    logger.addHandler(st_handler)
    return logger

def load_documents(json_path):
    with open(json_path, "r") as f:
        raw_docs = json.load(f)

    cat_documents = [f"{doc['title']}:{doc['content']}" for doc in raw_docs]
    return cat_documents