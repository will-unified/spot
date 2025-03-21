# python imports
import os
from dotenv import load_dotenv, find_dotenv

# local imports
from spot.api import SpotifyApi
from spot.album import SpotifyAlbum

# Load environment variables from .env file
load_dotenv(find_dotenv(), override=True)

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# auth
api = SpotifyApi(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
token_data = api.login()

# NOTE: this is where you would save the token_data to a file or database

album_api = SpotifyAlbum(api)
result = album_api.search_by_upc("9353450599244")

albums = result.get("albums", {}).get("items", [])
if albums:
    album = albums[0]
    print(album["name"], "-", album["artists"][0]["name"])
else:
    print("No album found for that UPC.")
