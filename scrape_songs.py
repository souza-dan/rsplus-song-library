import csv
import os
from datetime import datetime

from genres import get_genres
from songs import fetch_songs
import logging


def write_to_csv(songs, filename, output_dir="outputs"):
    with (open(os.path.join(output_dir, filename), mode='w', newline='', encoding='utf-8') as file):
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
            songId = song['songId']
            song_name = song['songName']
            artist = song['artistName']
            album = song['albumName']
            genre = song['genre']
            year = song['songYear']
            song_length = song['songLength']

            hasUGCGuitarArrangement = song['hasUGCGuitarArrangement']
            hasUGCBassArrangement = song['hasUGCBassArrangement']
            hasUGCPianoArrangement = song['hasUGCPianoArrangement']
            hasOfficialGuitarArrangement = song['hasOfficialGuitarArrangement']
            hasOfficialBassArrangement = song['hasOfficialBassArrangement']
            hasOfficialPianoArrangement = song['hasOfficialPianoArrangement']

            writer.writerow([
                songId,
                song_name,
                artist,
                album,
                genre,
                year,
                song_length,
                hasUGCGuitarArrangement,
                hasUGCBassArrangement,
                hasUGCPianoArrangement,
                hasOfficialGuitarArrangement,
                hasOfficialBassArrangement,
                hasOfficialPianoArrangement,
            ])

def main():
    page_size = 25  # Max page size

    # For now, this stores all the songs in memory in a dictionary keyed by songId
    # Currently, there are fewer than 10k songs, which fits w
    all_songs = {}

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
    write_to_csv(all_songs.values(), song_filename)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    main()
