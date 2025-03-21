# python imports
import os
from dotenv import load_dotenv, find_dotenv

# local imports
from spot.api import SpotifyApi
from spot.track import SpotifyTrack

# Load environment variables from .env file
load_dotenv(find_dotenv(), override=True)

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# auth
api = SpotifyApi(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
token_data = api.login()

# Search for a track by ISRC
track_api = SpotifyTrack(api)
result = track_api.search_by_isrc("AUI442500025")

tracks = result.get("tracks", {}).get("items", [])
if tracks:
    print(tracks[0]["name"], "-", tracks[0]["artists"][0]["name"])
else:
    print("No track found for that ISRC.")
