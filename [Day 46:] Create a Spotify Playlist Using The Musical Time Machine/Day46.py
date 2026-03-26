# Billboard Hot 100 -> Spotify Playlist (Musical Time Machine)

import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

# --- User Input ---
date = input("Which year do you want to travel to? Enter a date (YYYY-MM-DD): ")

# --- Scrape Billboard Hot 100 ---
url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(response.text, "html.parser")

song_titles = [tag.get_text(strip=True) for tag in soup.select("li ul li h3#title-of-a-story")]

if not song_titles:
    print("No songs found. The date may be invalid or the page structure has changed.")
    exit()

print(f"\nFound {len(song_titles)} songs from {date}:")
for i, title in enumerate(song_titles[:5], 1):
    print(f"  {i}. {title}")
print("  ...")

# --- Spotify Auth ---
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("SPOTIFY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
        redirect_uri="https://example.com",
        scope="playlist-modify-private",
        cache_path=".spotify_cache",
        open_browser=False,
    )
)

user_id = sp.current_user()["id"]

# --- Search for each song on Spotify ---
year = date.split("-")[0]
track_uris = []

for title in song_titles:
    result = sp.search(q=f"track:{title} year:{year}", type="track", limit=1)
    tracks = result["tracks"]["items"]
    if tracks:
        track_uris.append(tracks[0]["uri"])
    else:
        print(f"Could not find: {title}")

print(f"\nMatched {len(track_uris)} / {len(song_titles)} songs on Spotify.")

# --- Create Playlist ---
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"Billboard Hot 100 - {date}",
    public=False,
    description=f"Top songs from Billboard Hot 100 on {date}",
)

sp.playlist_add_items(playlist["id"], track_uris)

print(f"\nPlaylist created: {playlist['external_urls']['spotify']}")
