from datetime import datetime
from logic.logic import competition_is_not_past


COMPETITION_DATE = "2025-01-01 12:00:00"


def test_booking_allowed_when_today_before_competition():
    today = datetime(2024, 12, 31, 12, 0, 0)
    assert competition_is_not_past(COMPETITION_DATE, today) is True


def test_booking_refused_when_today_after_competition():
    today = datetime(2025, 1, 2, 12, 0, 0)
    assert competition_is_not_past(COMPETITION_DATE, today) is False


def test_booking_refused_when_today_same_day_but_time_passed():
    today = datetime(2025, 1, 1, 15, 0, 0)
    assert competition_is_not_past(COMPETITION_DATE, today) is False


def test_booking_allowed_when_today_same_day_but_time_before():
    today = datetime(2025, 1, 1, 10, 0, 0)
    assert competition_is_not_past(COMPETITION_DATE, today) is True
