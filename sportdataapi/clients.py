from datetime import date
import requests


SOCCER_ENDPOINT = "https://app.sportdataapi.com/api/v1/soccer"


class SoccerClient:

    def __init__(self, key, endpoint=SOCCER_ENDPOINT):
        self._key = key
        self._endpoint = endpoint

    def get_matches(self, season_id, date_from=None, date_to=None):
        """Get matches for a given season."""
        params = {"season_id": season_id}
        if date_from is not None:
            params["date_from"] = "{:%Y-%m-%d}".format(date_from)
        if date_to is not None:
            params["date_to"] = "{:%Y-%m-%d}".format(date_to)
        return self._get("matches", **params)["data"]
        
    def get_match(self, match_id):
        """Get match details."""
        return self._get(f"matches/{match_id}")["data"]

    def get_odds(self, match_id, type):
        """Get bookmakers' odds for a match."""
        return self._get(f"odds/{match_id}", type=type)["data"]

    def get_status(self):
        """Get account status."""
        return self._get("status")

    def _get(self, method, **params):
        headers = {"apikey": self._key}
        url = "{}/{}".format(self._endpoint, method)
        res = requests.get(url, headers=headers, params=params)
        return res.json()
