from unittest.mock import patch
import json
from datetime import datetime, timedelta
import server


def test_data_persistence_real(tmp_path, client):
    clubs_file = tmp_path / "clubs.json"
    competitions_file = tmp_path / "competitions.json"

    clubs = [{"name": "Club Test", "points": 10, "email": "test@mail.com"}]
    competitions = [{
        "name": "Spring Festival",
        "date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"),
        "numberOfPlaces": 25
    }]

    clubs_file.write_text(json.dumps({"clubs": clubs}, indent=4))
    competitions_file.write_text(json.dumps({"competitions": competitions}, indent=4))

    server.clubs = clubs
    server.competitions = competitions

    def open_mock(path, mode="r", *args, **kwargs):
        if "clubs.json" in path:
            return open(clubs_file, mode, *args, **kwargs)
        elif "competitions.json" in path:
            return open(competitions_file, mode, *args, **kwargs)
        else:
            return open(path, mode, *args, **kwargs)

    with patch("logic.logic.open", new=open_mock):
        client.post("/purchasePlaces", data={
            "club": "Club Test",
            "competition": "Spring Festival",
            "places": "4"
        })

    saved_clubs = json.loads(clubs_file.read_text())["clubs"]
    saved_competitions = json.loads(competitions_file.read_text())["competitions"]

    assert saved_clubs[0]["points"] == 6
    assert saved_competitions[0]["numberOfPlaces"] == 21
