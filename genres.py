import requests
import logging
from typing import List


def get_genres() -> List[str]:
    url = "https://ugc-retail-publicapi.ib.ubi.com/v1/songLibrary/getTypesOfGenre"
    response = requests.get(url)

    if response.status_code == 200:
        genres_data = response.json().get('data', [])
        return genres_data
    else:
        logging.error("Failed to retrieve genres. Status code: %s", response.status_code)
        return []
