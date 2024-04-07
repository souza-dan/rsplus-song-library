# rsplus-song-library
Helper scripts for downloading the [song library for Rocksmith+](https://www.ubisoft.com/en-gb/game/rocksmith/plus/song-library) from the Ubisoft APIs.

# Requirements
To use this program, make sure you have Python 3 installed and the required libraries (json, os, requests, time, and urllib.parse) are available. Run `pip install -r requirements.txt` to install the required libraries.

# Usage
```
python scrape_songs.py
```

This will create a csv file in the `outputs` directory with a CSV of the available songs in Rocksmith+.

API requests are cached in the `requests` directory. To get re-fetch results from the APIs after running once, delete the `requests` directory.

# Example Output
```csv
Song ID,Song Name,Artist,Album,Genre,Year,Duration,hasUGCGuitarArrangement,hasUGCBassArrangement,hasUGCPianoArrangement,hasOfficialGuitarArrangement,hasOfficialBassArrangement,hasOfficialPianoArrangement
fc6c92a7-2656-9122-4c9d-50cdadef466a,25:15,Bobby McFerrin,spirityouall,"Blues,Sacred Music",2013,238.0,False,False,False,False,False,False
41072537-25ef-dc80-64fa-cd1f2085ef82,Ain't No Sunshine,Al Jarreau,Back To Back Legends,"R&B,Blues",2008,127.0,False,False,False,False,False,False
070919d8-6931-3092-8cea-0d8808580ddf,Ain't That a Lot of Love,The Fabulous Thunderbirds,The Essential Fabulous Thunderbirds,"Pop,Rock,Blues",1991,225.0,False,False,False,True,True,False
```

# License
This project is licensed under the terms of the MIT license.

