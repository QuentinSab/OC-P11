import server


def test_booking_fails_when_requesting_more_than_available(client):
    server.clubs = [{"name": "Club Test", "points": 10}]
    server.competitions = [{"name": "Spring Festival", "numberOfPlaces": 5}]

    response = client.post(
        "/purchasePlaces",
        data={"club": "Club Test", "competition": "Spring Festival", "places": "8"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Pas assez de places disponibles." in response.data


def test_booking_succeeds_when_requesting_up_to_available_places(client):
    server.clubs = [{"name": "Club Test", "points": 10}]
    server.competitions = [{"name": "Spring Festival", "numberOfPlaces": 5}]

    response = client.post(
        "/purchasePlaces",
        data={"club": "Club Test", "competition": "Spring Festival", "places": "5"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Les places ont bien ete reservees." in response.data


def test_booking_succeeds_when_requesting_less_than_available_places(client):
    server.clubs = [{"name": "Club Test", "points": 10}]
    server.competitions = [{"name": "Spring Festival", "numberOfPlaces": 5}]

    response = client.post(
        "/purchasePlaces",
        data={"club": "Club Test", "competition": "Spring Festival", "places": "3"},
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Les places ont bien ete reservees." in response.data
