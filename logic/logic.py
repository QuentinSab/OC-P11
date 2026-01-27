import json


def loadClubs():
    with open("clubs.json") as c:
        listOfClubs = json.load(c)["clubs"]
        return listOfClubs


def loadCompetitions():
    with open("competitions.json") as comps:
        listOfCompetitions = json.load(comps)["competitions"]
        return listOfCompetitions


def get_club_by_email(email, clubs):
    for club in clubs:
        if club["email"] == email:
            return club
    return None


def can_book_places(club, places_requested):
    return int(club["points"]) >= places_requested


def has_enough_places(competition, places_requested):
    return int(places_requested) <= int(competition["numberOfPlaces"])
