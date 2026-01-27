from logic.logic import has_enough_places


def test_booking_fails_when_requested_more_than_available():
    competition = {"name": "Spring Festival", "numberOfPlaces": "5"}
    assert has_enough_places(competition, 8) is False


def test_booking_succeeds_when_requested_equals_available():
    competition = {"name": "Spring Festival", "numberOfPlaces": "5"}
    assert has_enough_places(competition, 5) is True


def test_booking_succeeds_when_requested_less_than_available():
    competition = {"name": "Spring Festival", "numberOfPlaces": "5"}
    assert has_enough_places(competition, 3) is True


def test_number_of_places_as_string_is_handled():
    competition = {"name": "Spring Festival", "numberOfPlaces": "5"}
    assert has_enough_places(competition, "3") is True
