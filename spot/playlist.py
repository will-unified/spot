from typing import Optional, Dict, Any, List
from .api import SpotifyApi


class SpotifyPlaylist:
    def __init__(self, api: SpotifyApi):
        self.api = api

    def get(self, playlist_id: str) -> Dict:
        return self.api.get(f"/playlists/{playlist_id}")

    def change_details(
        self,
        playlist_id: str,
        name: Optional[str] = None,
        public: Optional[bool] = None,
        collaborative: Optional[bool] = None,
        description: Optional[str] = None,
    ) -> None:
        """
        Change a playlist's name and public/private state.
        https://developer.spotify.com/documentation/web-api/reference/playlists/change-playlist-details/
        """
        data = {}
        if name:
            data["name"] = name
        if public is not None:
            data["public"] = public
        if collaborative is not None:
            data["collaborative"] = collaborative
        if description:
            data["description"] = description
        self.api.put(f"/playlists/{playlist_id}", data=data)

    def get_items(
        self,
        playlist_id: str,
        limit: int = 100,
        offset: int = 0,
        fields: Optional[str] = None,
        market: Optional[str] = None,
    ) -> Dict:
        params = {"limit": limit, "offset": offset}
        if fields:
            params["fields"] = fields
        if market:
            params["market"] = market
        return self.api.get(f"/playlists/{playlist_id}/tracks", params=params)

    def replace_playlist_items(self, playlist_id: str, uris: List[str]) -> None:
        """
        Replace all items in a playlist.
        https://developer.spotify.com/documentation/web-api/reference/playlists/replace-playlists-tracks/
        Max 100 URIs.
        """
        data = {"uris": uris}
        self.api.put(f"/playlists/{playlist_id}/tracks", data=data)

    def add_playlist_items(
        self, playlist_id: str, uris: List[str], position: Optional[int] = None
    ) -> None:
        """
        Add items to a playlist.
        https://developer.spotify.com/documentation/web-api/reference/playlists/add-tracks-to-playlist/
        Max 100 URIs.
        """
        data = {"uris": uris}
        if position is not None:
            data["position"] = position
        self.api.post(f"/playlists/{playlist_id}/tracks", data=data)

    def remove_playlist_items(
        self, playlist_id: str, uris: List[str], snapshot_id: Optional[str] = None
    ) -> None:
        """
        Remove items from a playlist.
        https://developer.spotify.com/documentation/web-api/reference/playlists/remove-tracks-playlist/
        Max 100 URIs.
        """
        data = {"tracks": [{"uri": uri} for uri in uris]}
        if snapshot_id:
            data["snapshot_id"] = snapshot_id
        self.api.delete(f"/playlists/{playlist_id}/tracks", data=data)

    def get_current_user_playlists(self, limit: int = 20, offset: int = 0) -> Dict:
        params = {"limit": limit, "offset": offset}
        return self.api.get("/me/playlists", params=params)

    def get_users_playlists(
        self, user_id: str, limit: int = 20, offset: int = 0
    ) -> Dict:
        params = {"limit": limit, "offset": offset}
        return self.api.get(f"/users/{user_id}/playlists", params=params)

    def create_playlist(
        self,
        user_id: str,
        name: str,
        public: Optional[bool] = None,
        collaborative: Optional[bool] = None,
        description: Optional[str] = None,
    ) -> Dict:
        data = {"name": name}
        if public is not None:
            data["public"] = public
        if collaborative is not None:
            data["collaborative"] = collaborative
        if description:
            data["description"] = description
        return self.api.post(f"/users/{user_id}/playlists", data=data)

    def get_playlist_cover_image(self, playlist_id: str) -> List[Dict]:
        return self.api.get(f"/playlists/{playlist_id}/images")

    def upload_playlist_cover_image(self, playlist_id: str, image: bytes) -> None:
        """
        Upload a custom playlist cover image.
        https://developer.spotify.com/documentation/web-api/reference/upload-custom-playlist-cover

        - The image must be JPEG format.
        - The image must be base64-encoded (not URL-safe encoding).
        - Max size: 256 KB.
        """
        self.api.put(
            f"/playlists/{playlist_id}/images", data=image, content_type="image/jpeg"
        )
