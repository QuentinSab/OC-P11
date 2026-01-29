from datetime import datetime
import json


def loadClubs():
    with open("clubs.json") as c:
        listOfClubs = json.load(c)["clubs"]
        return listOfClubs


def loadCompetitions():
    with open("competitions.json") as comps:
        listOfCompetitions = json.load(comps)["competitions"]
        return listOfCompetitions


def saveClubs(clubs, path="clubs.json"):
    with open(path, "w") as c:
        json.dump({"clubs": clubs}, c, indent=4)


def saveCompetitions(competitions, path="competitions.json"):
    with open(path, "w") as comps:
        json.dump({"competitions": competitions}, comps, indent=4)


def get_club_by_email(email, clubs):
    for club in clubs:
        if club["email"] == email:
            return club
    return None


def can_book_places(club, places_requested):
    return int(club["points"]) >= places_requested


def has_enough_places(competition, places_requested):
    return int(places_requested) <= int(competition["numberOfPlaces"])


def respects_max_places_per_booking(places_requested, max_places=12):
    return int(places_requested) <= max_places


def competition_is_not_past(competition_date_str, today=None):
    if today is None:
        today = datetime.now()

    competition_date = datetime.strptime(competition_date_str, "%Y-%m-%d %H:%M:%S")
    return competition_date > today
