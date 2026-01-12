def get_club_by_email(email, clubs):
    for club in clubs:
        if club["email"] == email:
            return club
    return None
