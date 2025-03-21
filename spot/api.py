# spotify_api.py

import requests
import time
from typing import Optional, Dict, Any


class SpotifyApi:
    AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
    TOKEN_URL = "https://accounts.spotify.com/api/token"
    BASE_API_URL = "https://api.spotify.com/v1"

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        redirect_uri: Optional[str] = None,
        access_token: Optional[str] = None,
        refresh_token: Optional[str] = None,
        token_expires_at: Optional[float] = None,
    ):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.token_expires_at = token_expires_at

    def build_authorize_url(
        self, scopes: list[str], state: Optional[str] = None
    ) -> str:
        query_params = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": self.redirect_uri,
            "scope": " ".join(scopes),
        }
        if state:
            query_params["state"] = state
        return f"{self.AUTHORIZE_URL}?{requests.compat.urlencode(query_params)}"

    def exchange_code_for_token(self, code: str) -> Dict[str, Any]:
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.redirect_uri,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        response = requests.post(self.TOKEN_URL, data=data)
        response.raise_for_status()
        token_data = response.json()

        self.access_token = token_data["access_token"]
        self.refresh_token = token_data.get("refresh_token")
        expires_in = token_data["expires_in"]
        self.token_expires_at = time.time() + expires_in - 60

        return token_data

    def refresh_access_token(self) -> Dict[str, Any]:
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }
        response = requests.post(self.TOKEN_URL, data=data)
        response.raise_for_status()
        token_data = response.json()

        self.access_token = token_data["access_token"]
        expires_in = token_data["expires_in"]
        self.token_expires_at = time.time() + expires_in - 60
        return token_data

    def _get_headers(self) -> Dict[str, str]:
        if not self.access_token:
            raise ValueError("Access token is required to make requests.")
        return {"Authorization": f"Bearer {self.access_token}"}

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict:
        url = f"{self.BASE_API_URL}{endpoint}"
        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()

    def post(
        self,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Dict:
        url = f"{self.BASE_API_URL}{endpoint}"
        response = requests.post(url, headers=self._get_headers(), data=data, json=json)
        response.raise_for_status()
        return response.json()
