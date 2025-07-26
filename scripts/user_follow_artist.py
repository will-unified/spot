# python imports
import os
from dotenv import load_dotenv, find_dotenv

# local imports
from spot.api import SpotifyApi
from spot.user import SpotifyUser

# Load environment variables from .env file
load_dotenv(find_dotenv(), override=True)

LINKS_CLIENT_ID = os.getenv("LINKS_CLIENT_ID")
LINKS_CLIENT_SECRET = os.getenv("LINKS_CLIENT_SECRET")
LINKS_SPOTIFY_TOKEN = os.getenv("LINKS_SPOTIFY_TOKEN")

# auth
api = SpotifyApi(
    client_id=LINKS_CLIENT_ID,
    client_secret=LINKS_CLIENT_SECRET,
    access_token=LINKS_SPOTIFY_TOKEN,
)

user_api = SpotifyUser(api)

# Follow an artist
artist_id = "6f5yObGSpFj9eJL55GBzrb"  # LANKS
user_api.follow_artist(artist_id)
print(f"Followed artist with ID: {artist_id}")

# Follow a playlist
playlist_id = "7yAwfIUrQg5kSG6AIiocx1"  # Listen to LANKS
user_api.follow_playlist(playlist_id)
print(f"Followed playlist with ID: {playlist_id}")

# Save an album
album_id = "6Ehy4ljHT4eEVBZboxyoXU"  # LANKS - Inoue EP
user_api.save_album(album_id)
print(f"Saved album with ID: {album_id}")

# Save a Track
track_id = "5R0tCly0GgsCCYmhy8hpgq"  # LANKS - Stronger Than
user_api.save_track(track_id)
print(f"Saved track with ID: {track_id}")
