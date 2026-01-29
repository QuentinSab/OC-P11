import server
from datetime import datetime, timedelta


def test_booking_fails_when_requesting_more_than_12_places(client):
    server.clubs = [
        {"name": "Club Test", "points": 20}
    ]
    server.competitions = [{
        "name": "Spring Festival",
        "numberOfPlaces": 30,
        "date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    }]

    response = client.post(
        "/purchasePlaces",
        data={
            "club": "Club Test",
            "competition": "Spring Festival",
            "places": "13"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Impossible de reserver plus de 12 places a la fois." in response.data


def test_booking_succeeds_when_requesting_12_places(client):
    server.clubs = [
        {"name": "Club Test", "points": 20}
    ]
    server.competitions = [{
        "name": "Spring Festival",
        "numberOfPlaces": 30,
        "date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    }]

    response = client.post(
        "/purchasePlaces",
        data={
            "club": "Club Test",
            "competition": "Spring Festival",
            "places": "12"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Les places ont bien ete reservees." in response.data


def test_booking_succeeds_when_requesting_less_than_12_places(client):
    server.clubs = [
        {"name": "Club Test", "points": 20}
    ]
    server.competitions = [{
        "name": "Spring Festival",
        "numberOfPlaces": 30,
        "date": (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    }]

    response = client.post(
        "/purchasePlaces",
        data={
            "club": "Club Test",
            "competition": "Spring Festival",
            "places": "6"
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Les places ont bien ete reservees." in response.data
