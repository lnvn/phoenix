import logging
import requests
from config import config


def main():
    logging.info("START")
    google_api_key = config["google_api_key"]
    response = requests.get("https://www.googleapis.com/youtube/v3/playlistItems", params={
        'key': google_api_key,
        'playlistId': '',
    })
    logging.debug('Got %s', response.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()