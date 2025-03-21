# python imports
import os
from dotenv import load_dotenv, find_dotenv

# local imports
from spot.api import SpotifyApi
from spot.artist import SpotifyArtist

# Load environment variables from .env file
load_dotenv(find_dotenv(), override=True)

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# auth
api = SpotifyApi(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
token_data = api.login()

# NOTE: this is where you would save the token_data to a file or database


# Initialize SpotifyArtist
artist_api = SpotifyArtist(api)

# # Get Artist
# artist_data = artist_api.get("6f5yObGSpFj9eJL55GBzrb")
# # print(f"artist_data: {artist_data}")

# # Get Artist Albums
# albums_data = artist_api.albums("6f5yObGSpFj9eJL55GBzrb")
# # print(f"albums_data: {albums_data}")

# Get Artist Top Tracks
top_tracks_data = artist_api.top_tracks("6f5yObGSpFj9eJL55GBzrb")
# for track in top_tracks_data["tracks"]:
#     print(f"{track['name']} - {track['popularity']}")
