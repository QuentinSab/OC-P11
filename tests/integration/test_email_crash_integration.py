def test_show_summary_with_valid_email_returns_welcome(client):
    response = client.post(
        "/showSummary",
        data={"email": "john@simplylift.co"},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Welcome" in response.data


def test_show_summary_with_invalid_email_flashes_message(client):
    response = client.post(
        "/showSummary",
        data={"email": "invalid@email"},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Email invalide" in response.data
