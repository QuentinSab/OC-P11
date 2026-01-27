from logic.logic import respects_max_places_per_booking


def test_booking_fails_when_requesting_more_than_12_places():
    assert respects_max_places_per_booking(13) is False


def test_booking_succeeds_when_requesting_12_places():
    assert respects_max_places_per_booking(12) is True


def test_booking_succeeds_when_requesting_less_than_12_places():
    assert respects_max_places_per_booking(5) is True


def test_booking_handles_string_input():
    assert respects_max_places_per_booking("10") is True
