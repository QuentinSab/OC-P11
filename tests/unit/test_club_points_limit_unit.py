from logic.logic import can_book_places


def test_can_book_when_enough_points():
    club = {"points": 10}
    assert can_book_places(club, 5) is True


def test_cannot_book_when_not_enough_points():
    club = {"points": 3}
    assert can_book_places(club, 5) is False
