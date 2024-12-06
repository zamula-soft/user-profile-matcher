import logging
import os
import sys


def get_postgres_uri():
    host = os.environ.get("DB_HOST", "localhost")
    port = 54321 if host == "localhost" else 5432
    password = os.environ.get("DB_PASSWORD", "postgres")
    user, db_name = "postgres", "postgres"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


def get_api_url():
    host = os.environ.get("API_HOST", "localhost")
    port = 5005 if host == "localhost" else 80
    return f"http://{host}:{port}"


def get_logger(name):
    LOGGING_LEVEL = logging.DEBUG
    logging.basicConfig(stream=sys.stdout, level=LOGGING_LEVEL)

    return logging.getLogger(name)
