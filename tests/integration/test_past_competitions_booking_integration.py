import server
from datetime import datetime, timedelta


def test_booking_fails_when_competition_in_past(client):
    server.clubs = [{"name": "Club Test", "points": 10}]

    past_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    server.competitions = [{"name": "Spring Festival", "numberOfPlaces": 25, "date": past_date}]

    response = client.post(
        "/purchasePlaces",
        data={
            "club": "Club Test",
            "competition": "Spring Festival",
            "places": "2"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Impossible de reserver pour une competition passee." in response.data


def test_booking_succeeds_when_competition_in_future(client):
    server.clubs = [{"name": "Club Test", "points": 10}]

    future_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    server.competitions = [{"name": "Spring Festival", "numberOfPlaces": 25, "date": future_date}]

    response = client.post(
        "/purchasePlaces",
        data={
            "club": "Club Test",
            "competition": "Spring Festival",
            "places": "2"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Les places ont bien ete reservees." in response.data
