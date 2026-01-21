import server


def test_book_places_fails_when_not_enough_points(client):
    server.clubs = [
        {"name": "Club Test", "points": 10}
    ]
    server.competitions = [
        {"name": "Spring Festival", "numberOfPlaces": 25}
    ]

    response = client.post(
        "/purchasePlaces",
        data={
            "club": "Club Test",
            "competition": "Spring Festival",
            "places": "20"
        },
        follow_redirects=True
    )

    assert b"Pas assez de points disponibles." in response.data


def test_book_places_succeeds_when_enough_points(client):
    server.clubs = [
        {"name": "Club Test", "points": 10}
    ]
    server.competitions = [
        {"name": "Spring Festival", "numberOfPlaces": 25}
    ]

    response = client.post(
        "/purchasePlaces",
        data={
            "club": "Club Test",
            "competition": "Spring Festival",
            "places": "4"
        },
        follow_redirects=True
    )

    assert b"Les places ont bien ete reservees." in response.data
