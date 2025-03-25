import os
import time
import webbrowser
from dotenv import load_dotenv, find_dotenv
from spot.api import SpotifyApi
from spot.album import SpotifyAlbum
from spot.track import SpotifyTrack

# Load environment variables from .env
load_dotenv(find_dotenv(), override=True)

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")  # e.g. "http://localhost:8080/callback"

# Step 1: Initialize Spotify API with app credentials
api = SpotifyApi(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
)

# Step 2: Generate auth URL and open it
scopes = ["user-library-read", "playlist-modify-private", "playlist-modify-public"]
auth_url = api.build_authorize_url(scopes=scopes, state="test")

print("Opening browser to authenticate with Spotify...")
webbrowser.open(auth_url)

# Step 3: User will be redirected to something like:
# http://localhost:8080/callback?code=AQAK...xyz
# Copy the `code` from the URL and paste it below 👇
code = input("Paste the authorization code from the redirect URL: ")

# Step 4: Exchange code for access + refresh token
token_data = api.exchange_code_for_token(code)

# You could save token_data to a file or DB here
print("Access token:", token_data["access_token"])

# Step 5: Use the API
track_api = SpotifyTrack(api)
track_data = track_api.get("0nNDLjah0PaOFn2j7sMsF0")
print(f"track_data: {track_data}")
