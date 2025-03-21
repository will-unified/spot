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

# NOTE: this is where you would save the token_data to a file or database

track_api = SpotifyTrack(api)

# Multiple artists
ids = ["0nNDLjah0PaOFn2j7sMsF0", "7933VjnlxYm4Rvq8jZXiI1"]  # Say It, Time to Go
tracks = track_api.get_multiple(ids)

for track in tracks["tracks"]:
    print(track)
