import json
from flask import Flask, render_template, request, redirect, flash, url_for


def loadClubs():
    with open("clubs.json") as c:
        listOfClubs = json.load(c)["clubs"]
        return listOfClubs


def loadCompetitions():
    with open("competitions.json") as comps:
        listOfCompetitions = json.load(comps)["competitions"]
        return listOfCompetitions


# Nouvelle fonction pour mettre à jour les places
def update_places(competition: dict, places_required: int, club: dict) -> bool:
    nbr_places = int(competition["numberOfPlaces"])
    club_nbr_points = int(club["points"])
    if (0 < places_required < 13) and (places_required <= club_nbr_points):
        competition_places = nbr_places - places_required
        if competition_places < 0:
            return False
        competition["numberOfPlaces"] = competition_places
        club_nbr_points = club_nbr_points - places_required
        club["points"] = str(club_nbr_points)
        return True
    else:
        return False


app = Flask(__name__)
app.secret_key = "something_special"

competitions = loadCompetitions()
clubs = loadClubs()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/showSummary", methods=["POST"])
def showSummary():
    club = [club for club in clubs if club["email"] == request.form["email"]][0]
    return render_template("welcome.html", club=club, competitions=competitions)


# Route modifiée pour la réservation
@app.route("/book/<competition>/<club>")
def book(competition, club):
    foundClub = [c for c in clubs if c["name"] == club][0]
    foundCompetition = [c for c in competitions if c["name"] == competition][0]
    if foundClub and foundCompetition:
        max_places = min(
            12, int(foundClub["points"]), int(foundCompetition["numberOfPlaces"])
        )
        return render_template(
            "booking.html",
            club=foundClub,
            competition=foundCompetition,
            max_places=max_places,
        )
    else:
        flash("Something went wrong-please try again")
        return render_template("welcome.html", club=club, competitions=competitions)


@app.route("/purchasePlaces", methods=["POST"])
def purchasePlaces():
    # Vous pouvez utiliser la fonction update_places ici pour mettre à jour les places
    competition = [c for c in competitions if c["name"] == request.form["competition"]][
        0
    ]
    club = [c for c in clubs if c["name"] == request.form["club"]][0]
    placesRequired = int(request.form["places"])
    if update_places(competition, placesRequired, club):
        flash("Great-booking complete!")
    else:
        flash("Booking failed. Please check the number of places and points.")
    return render_template("welcome.html", club=club, competitions=competitions)


@app.route("/logout")
def logout():
    return redirect(url_for("index"))
