import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from config import CLIENT_ID, CLIENT_SECRET

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}
user_id = "31a2anz2umgvojgrnxyvrci2kkpi"


def get_date():
    date = input(
        "Which year do you want to travel to? Type date in format YYYY-MM-DD: "
    )
    return date


timestamp = get_date()

url = "https://www.billboard.com/charts/hot-100/"

response = requests.get(url=f"{url}{timestamp}/", headers=header)
response.raise_for_status()
billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage, "html.parser")

titles = [title.text.strip() for title in soup.select(selector="li ul li h3")]
artists = [
    artist.text.strip()
    for artist in soup.select(selector="li ul li span.c-label.a-no-trucate")
]
queries = [f"{artists[x]}, {titles[x]}" for x in range(len(titles))]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="https://example.com",
        scope="playlist-modify-private",
    )
)


spotify_endpoint = f"https://api.spotify.com/v1/users/{user_id}/playlists"

playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{timestamp} playlist",
    public=False,
    collaborative=False,
    description=f"top 100 songs from {timestamp}",
)

tracks_uris = []
for song in queries:
    song_data = sp.search(song, limit=2)
    try:
        song_uri = song_data["tracks"]["items"][0]["uri"]
        tracks_uris.append(song_uri)
    except:
        print(f"missing: {song}")


sp.playlist_add_items(playlist_id=playlist["id"], items=tracks_uris)
