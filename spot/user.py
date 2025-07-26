# user.py

from typing import Dict, Any
from .api import SpotifyApi


class SpotifyUser:
    def __init__(self, api: SpotifyApi):
        self.api = api

    def get_profile(self) -> Dict[str, Any]:
        """
        Get the authenticated user's profile, including email.
        https://developer.spotify.com/documentation/web-api/reference/get-current-users-profile
        """
        return self.api.get("/me")

    def get_recently_played(self, limit: int = 20) -> Dict:
        """
        Get the user's recently played tracks.
        """
        return self.api.get("/me/player/recently-played", params={"limit": limit})

    def get_top_items(
        self,
        item_type: str = "tracks",
        time_range: str = "medium_term",
        limit: int = 20,
    ) -> Dict:
        """
        Get user's top artists or tracks.
        item_type: "artists" or "tracks"
        time_range: short_term (4 weeks), medium_term (6 months), long_term (several years)
        """
        return self.api.get(
            f"/me/top/{item_type}", params={"time_range": time_range, "limit": limit}
        )

    def follow_artist(self, artist_id: str) -> None:
        """
        Follow a single artist.
        https://developer.spotify.com/documentation/web-api/reference/follow-artists-users
        """
        self.api.put("/me/following", params={"type": "artist", "ids": artist_id})

    def follow_playlist(self, playlist_id: str) -> None:
        """
        Follow a playlist (i.e., subscribe).
        https://developer.spotify.com/documentation/web-api/reference/follow-playlist
        """
        self.api.put(f"/playlists/{playlist_id}/followers")

    def save_album(self, album_id: str) -> None:
        """
        Save an album to the user's library.
        https://developer.spotify.com/documentation/web-api/reference/save-albums-users
        """
        self.api.put("/me/albums", params={"ids": album_id})

    def save_track(self, track_id: str) -> None:
        """
        Save a track to the user's library.
        https://developer.spotify.com/documentation/web-api/reference/save-tracks-user
        """
        self.api.put("/me/tracks", params={"ids": track_id})
