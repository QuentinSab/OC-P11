import json
from logic.logic import saveClubs, saveCompetitions


def test_saveClubs(tmp_path):
    clubs = [{"name": "Club Test", "points": 10, "email": "test@mail.com"}]
    file_path = tmp_path / "clubs.json"

    saveClubs(clubs, path=file_path)

    saved_data = json.loads(file_path.read_text())
    assert "clubs" in saved_data
    assert saved_data["clubs"][0]["name"] == "Club Test"
    assert saved_data["clubs"][0]["points"] == 10
    assert saved_data["clubs"][0]["email"] == "test@mail.com"


def test_saveCompetitions(tmp_path):
    competitions = [{
        "name": "Spring Festival",
        "date": "2030-01-01 10:00:00",
        "numberOfPlaces": 20
    }]
    file_path = tmp_path / "competitions.json"

    saveCompetitions(competitions, path=file_path)

    saved_data = json.loads(file_path.read_text())
    assert "competitions" in saved_data
    assert saved_data["competitions"][0]["name"] == "Spring Festival"
    assert saved_data["competitions"][0]["date"] == "2030-01-01 10:00:00"
    assert saved_data["competitions"][0]["numberOfPlaces"] == 20
