import csv
import os
from datetime import datetime
from typing import List, Dict, Any

from genres import get_genres
from songs import fetch_songs
import logging


def extract_song_fields(song: Dict[str, Any]) -> List[Any]:
    """Songs have many fields; extract only the ones we care about."""

    """
    Example song:
    {
        "tempoMapLock": false,
        "bonusAvailable": 0,
        "videoRequest": 0,
        "albumImages": [
            {
                "albumImageId": "bc2e187b-4aff-45e1-8d9f-ec235163878a",
                "height": 1255,
                "width": 1400,
                "territoryCode": "worldwide"
            }
        ],
        "totalArrangements": 2,
        "hasUGCGuitarArrangement": false,
        "hasUGCBassArrangement": false,
        "hasUGCPianoArrangement": false,
        "hasOfficialGuitarArrangement": false,
        "hasOfficialBassArrangement": false,
        "hasOfficialPianoArrangement": false,
        "hasArrangementTypes": [
            11,
            10
        ],
        "lyrics": false,
        "lenghtFormatted": null,
        "verifiedTempo": true,
        "songId": "fc6c92a7-2656-9122-4c9d-50cdadef466a",
        "songName": "25:15",
        "songYear": 2013,
        "songLength": 238,
        "artistName": "Bobby McFerrin",
        "albumName": "spirityouall",
        "albumId": "d93a1bbf-9fbb-4e2c-9082-1cc3e4122395",
        "genre": "Blues,Sacred Music",
        "explicit": false,
        "isRegionallyRestricted": false,
        "isCover": false,
        "publishedwithin30days": false
    }
    """
    return [
        song['songId'],
        song['songName'],
        song['artistName'],
        song['albumName'],
        song['genre'],
        song['songYear'],
        song['songLength'],
        song['hasUGCGuitarArrangement'],
        song['hasUGCBassArrangement'],
        song['hasUGCPianoArrangement'],
        song['hasOfficialGuitarArrangement'],
        song['hasOfficialBassArrangement'],
        song['hasOfficialPianoArrangement'],
    ]


def write_to_csv(songs: List[Dict[str, Any]], filename: str, output_dir: str = "outputs") -> None:
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    with open(os.path.join(output_dir, filename), mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', lineterminator='\n')
        writer.writerow([
            'Song ID',
            'Song Name',
            'Artist',
            'Album',
            'Genre',
            'Year',
            'Duration',
            'hasUGCGuitarArrangement',
            'hasUGCBassArrangement',
            'hasUGCPianoArrangement',
            'hasOfficialGuitarArrangement',
            'hasOfficialBassArrangement',
            'hasOfficialPianoArrangement',
        ])
        for song in songs:
            writer.writerow(extract_song_fields(song))


def main() -> None:
    page_size = 25  # Max page size

    # For now, this stores all the songs in memory in a dictionary keyed by songId
    # Currently, there are fewer than 10k songs, which fits w
    all_songs: Dict[Any, Dict[str, Any]] = {}

    # Create a filename with the current date and time
    date_time_str = datetime.now().strftime("%Y%m%d-%H%M%S")
    song_filename = f"songs_{date_time_str}.csv"

    for genre in get_genres():
        page = 1  # Starting page
        # Fetch songs until there are no more pages left
        while True:
            songs = fetch_songs(page, page_size, genre)
            if not songs:
                break
            all_songs.update({song["songId"]: song for song in songs})
            page += 1

    # Write songs to CSV
    write_to_csv(list(all_songs.values()), song_filename)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
