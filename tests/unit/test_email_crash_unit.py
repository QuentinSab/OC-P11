from logic.logic import get_club_by_email


def test_get_club_with_valid_email():
    clubs = [{"email": "test@email.com"}]
    assert get_club_by_email("test@email.com", clubs) is not None


def test_get_club_with_invalid_email_returns_none():
    clubs = [{"email": "test@email.com"}]
    assert get_club_by_email("invalid@email", clubs) is None
