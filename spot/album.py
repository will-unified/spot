from typing import Dict, List
from .api import SpotifyApi


class SpotifyAlbum:
    def __init__(self, api: SpotifyApi):
        self.api = api

    def get(self, album_id: str) -> Dict:
        return self.api.get(f"/albums/{album_id}")

    def get_multiple(self, artist_ids: List[str]) -> Dict:
        """
        Get metadata for multiple albums (up to 50 at once).
        https://developer.spotify.com/documentation/web-api/reference/get-multiple-albums
        """
        ids_param = ",".join(artist_ids)
        return self.api.get("/albums", params={"ids": ids_param})

    def tracks(self, album_id: str) -> Dict:
        return self.api.get(f"/albums/{album_id}/tracks")

    def get_users_saved_albums(self, limit: int = 20, offset: int = 0) -> Dict:
        """
        Get a list of the albums saved in the current Spotify user’s library.
        https://developer.spotify.com/documentation/web-api/reference/library/get-users-saved-albums
        """
        params = {"limit": limit, "offset": offset}
        return self.api.get("/me/albums", params=params)

    def search_by_upc(self, upc: str) -> Dict:
        """
        Search for an album using a UPC (barcode).
        Returns a list of matching albums.
        https://developer.spotify.com/documentation/web-api/reference/search
        """
        query = f"upc:{upc}"
        params = {"q": query, "type": "album", "limit": 1}
        return self.api.get("/search", params=params)
