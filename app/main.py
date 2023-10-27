import logging

import requests

logging.basicConfig(level=logging.INFO)


def ping():
    response = requests.get("http://localhost:8000")
    logging.info("Response %s", response.json())
    return response.json()


if __name__ == '__main__':
    ping()
