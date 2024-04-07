import json
import logging
import os
import urllib

import requests
from random_sleep import random_sleep


def fetch_songs(page, page_size, genre, cache_directory="requests"):
    # Generate filename based on method arguments
    filename = f"genre_{genre}_page_{page}_page_size_{page_size}.json"

    # Check if cached file exists
    if os.path.exists(os.path.join(cache_directory, filename)):
        logging.info("Cached request - %s Page %s", genre, page)
        # If cached file exists, read content from the file
        with open(os.path.join(cache_directory, filename), 'r') as file:
            songs_data = json.load(file)
    else:
        logging.info("Fetch request - %s Page %s", genre, page)
        encoded_genre = urllib.parse.quote(genre)
        # If cached file doesn't exist, make the request
        url = f"https://ugc-retail-publicapi.ib.ubi.com/v1/songLibrary/songs?word=&sortKey=songName&descOrder=false&page={page}&pageSize={page_size}&genre={encoded_genre}"
        response = requests.get(url)

        if response.status_code == 200:
            songs_data = response.json().get('data', [])

            # Save content to a file for caching if something was returned
            os.makedirs(cache_directory, exist_ok=True)
            with open(os.path.join(cache_directory, filename), 'w') as file:
                json.dump(songs_data, file)
        else:
            print("Failed to retrieve songs. Status code:", response.status_code)
            songs_data = []

        # Wait between 0-1 seconds to not send too many requests too quickly
        random_sleep()

    return songs_data
