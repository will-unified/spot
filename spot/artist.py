from typing import Optional, Dict, Any, List
from .api import SpotifyApi


class SpotifyArtist:
    def __init__(self, api: SpotifyApi):
        self.api = api

    def get(self, artist_id: str) -> Dict:
        return self.api.get(f"/artists/{artist_id}")

    def get_multiple(self, artist_ids: List[str]) -> Dict:
        """
        Get metadata for multiple artists (up to 50 at once).
        https://developer.spotify.com/documentation/web-api/reference/get-multiple-artists
        """
        ids_param = ",".join(artist_ids)
        return self.api.get("/artists", params={"ids": ids_param})

    def albums(
        self,
        artist_id: str,
        include_groups: Optional[str] = None,
        market: Optional[str] = None,
        limit: int = 20,
        offset: int = 0,
    ) -> Dict:
        params = {"limit": limit, "offset": offset}
        if include_groups:
            params["include_groups"] = include_groups
        if market:
            params["market"] = market
        return self.api.get(f"/artists/{artist_id}/albums", params=params)

    def top_tracks(self, artist_id: str, market: Optional[str] = None) -> Dict:
        params = {}
        if market:
            params["market"] = market
        return self.api.get(f"/artists/{artist_id}/top-tracks", params=params)
