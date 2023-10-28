import json
from flask import Flask, render_template, request, redirect, flash, url_for


def load_clubs():
    with open('clubs.json') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


def load_competitions():
    with open('competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


app = Flask(__name__)
app.secret_key = "something_special"


def get_club_and_competition(club: str, competition: str) -> (bool, dict, dict):
    """Retrieve a club and a competition in the list, with their name

    param club: club name
    param competition: competition name
    return: True if they were found + objects
    """
    competition = [c for c in competitions if c['name'] == competition]
    club = [c for c in clubs if c['name'] == club]

    # Something wrong
    if not competition or not club:
        return False, None, None

    # No error
    return True, club[0], competition[0]


def update_places(competition: dict, places_required: int, club: dict) -> bool:
    """Book (and deduce) places in a given competition

    param competition: dictionary loaded from database and describing a competition
    param places_required: how many places the club wants to book
    return: True if the places could be booked
    """
    nbr_places = int(competition['numberOfPlaces'])
    club_nbr_points = int(club['points'])

    # Pay attention to the 12 places limit for each club, and the number of points available
    if (0 < places_required < 13) and (places_required <= club_nbr_points):
        competition_places = nbr_places - places_required
        # Make sure that the competition cannot run out of places
        if competition_places < 0:
            return False
        # Update values in both competition and club dictionaries
        competition['numberOfPlaces'] = competition_places
        club_nbr_points = club_nbr_points - places_required
        club['points'] = str(club_nbr_points)
        return True
    else:
        return False


competitions = load_competitions()
clubs = load_clubs()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def showSummary():
    club = [club for club in clubs if club["email"] == request.form["email"]][0]
    return render_template("welcome.html", club=club, competitions=competitions)


@app.route("/book/<competition>/<club>")
def book(competition, club):
    foundClub = [c for c in clubs if c["name"] == club][0]
    foundCompetition = [c for c in competitions if c["name"] == competition][0]
    if foundClub and foundCompetition:
        return render_template(
            "booking.html", club=foundClub, competition=foundCompetition
        )
    else:
        flash("Something went wrong-please try again")
        return render_template("welcome.html", club=club, competitions=competitions)


@app.route("/purchasePlaces", methods=["POST"])
def purchase_places():
    ok_flag, club, competition = get_club_and_competition(
        request.form["club"], request.form["competition"]
    )

    # Most probably some malicious attempt...
    if not ok_flag:
        return redirect("/")

    places_required = int(request.form["places"])

    if update_places(competition, places_required, club):
        flash("Great-booking complete!")
    else:
        flash("You tried to book an invalid number of places, sorry")

    return render_template("welcome.html", club=club, competitions=competitions)


# TODO: Add route for points display


@app.route("/logout")
def logout():
    return redirect(url_for("index"))
