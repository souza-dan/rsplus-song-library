import requests


def get_genres():
    url = "https://ugc-retail-publicapi.ib.ubi.com/v1/songLibrary/getTypesOfGenre"
    response = requests.get(url)

    if response.status_code == 200:
        genres_data = response.json().get('data', [])
        return genres_data
    else:
        print("Failed to retrieve genres. Status code:", response.status_code)
        return []


