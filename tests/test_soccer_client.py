import pytest
from datetime import datetime, date

from tutils import patch_post
from sportdataapi import SoccerClient


@pytest.fixture
def client(patch_post):
    return SoccerClient(key="DUMMY")


def test_get_matches(client):
    res = client.get_matches(
        season_id=496,
        date_from=date(2021, 4, 9),
        date_to=date(2021, 4, 15),
    )
    assert len(res) == 9
    assert res[4]["match_id"] == 178548
    assert res[4]["stats"] == {
        "home_score": 1,
        "away_score": 0,
        "ht_score": None,
        "ft_score": "1-0",
        "et_score": None,
        "ps_score": None,
    }


def test_get_match(client):
    idx = 178548
    res = client.get_match(idx)
    assert res["match_id"] == idx
    assert res["match_start_iso"] == "2021-04-11T13:30:00+00:00"
    assert res["stats"] == {
        "ht_score": None,
        "ft_score": "1-0",
        "et_score": None,
        "ps_score": None,
    }


def test_get_odds(client):
    idx = 178548
    res = client.get_odds(idx, type="prematch")
    assert res["1X2, Full Time Result"]["bookmakers"][1] == {
        "bookmaker_id": 1,
        "bookmaker_name": "10Bet",
        "odds_data": {
            "home": "3.000",
            "draw": "3.300",
            "away": "2.450",
            "handicap": None,
            "score": None,
            "minute": None,
            "over": None,
            "under": None,
        },
        "last_updated": "2021-04-11T10:56:04.000000Z",
    }


def test_get_status(client):
    res = client.get_status()
    assert res == {"remaining_requests": "99991"}
