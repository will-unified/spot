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

track_data = track_api.get("0nNDLjah0PaOFn2j7sMsF0")

print(f"track_data: {track_data}")
