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

artist_api = SpotifyArtist(api)

# Multiple artists
ids = ["6f5yObGSpFj9eJL55GBzrb", "5rar25ejTh6Z3bZ2MhiAfS"]  # LANKS, lindsay
artists = artist_api.get_multiple(ids)

for artist in artists["artists"]:
    print(artist)
