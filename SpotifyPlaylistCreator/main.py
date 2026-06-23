import os
import time

import spotipy
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret_code = os.getenv("SPOTIFY_CLIENT_SECRET_CODE")
redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret_code,
                                               redirect_uri=redirect_uri,
                                               scope="playlist-modify-private user-read-email",
                                               show_dialog=True
                                               ))

user_id = sp.current_user()["id"]

# print(user_id)

date = input("Which date would you like to travel to? Type the date in this format YYYY-MM--DD:\n")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
response= requests.get(f"https://appbrewery.github.io/bakeboard-hot-100/{date}/#",headers=header)
# 2026-04-18

bakeBoard_web_apy = response.text
soup = BeautifulSoup(bakeBoard_web_apy, "html.parser")

songs = soup.find_all(name="h3", attrs={"class": "chart-entry__title"})
song_titles = [song.getText().strip()  for song in songs]
# print(song_titles)


song_uris = []
year = date.split("-")[0]

for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} is not in Spotify. Skipped.")

    time.sleep(2)

print(song_uris)

playlist = sp.user_playlist_create(user=user_id,name=f"{date} Billboard Hot 100",public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"],items=song_uris)



