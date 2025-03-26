from typing import Optional, Dict, Any, List
from .api import SpotifyApi


class SpotifyTrack:
    def __init__(self, api: SpotifyApi):
        self.api = api

    def get(self, track_id: str) -> Dict:
        return self.api.get(f"/tracks/{track_id}")

    def get_multiple(self, track_ids: List[str]) -> Dict:
        """
        Get metadata for multiple tracks (up to 50 at once).
        https://developer.spotify.com/documentation/web-api/reference/get-multiple-tracks
        """
        ids_param = ",".join(track_ids)
        return self.api.get("/tracks", params={"ids": ids_param})

    def search_by_isrc(self, isrc: str) -> Dict:
        """
        Search for a track using an ISRC code.
        Returns a list of matching tracks.
        https://developer.spotify.com/documentation/web-api/reference/search
        """
        query = f"isrc:{isrc}"
        params = {
            "q": query,
            "type": "track",
            "limit": 1,  # You can increase this if you want more results
        }
        return self.api.get("/search", params=params)

    def search(self, query: str, limit: int = 10, offset: int = 0) -> Dict:
        """
        Search for tracks by name.
        https://developer.spotify.com/documentation/web-api/reference/search
        """
        params = {
            "q": query,
            "type": "track",
            "limit": limit,
            "offset": offset,
        }
        return self.api.get("/search", params=params)
