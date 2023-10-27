import json
from flask import Flask, render_template, request, redirect, flash, url_for


# Charger les données des clubs depuis un fichier JSON
def load_clubs():
    with open('clubs.json') as c:
        list_of_clubs = json.load(c)['clubs']
        return list_of_clubs


# Charger les données des compétitions depuis un fichier JSON
def load_competitions():
    with open('competitions.json') as comps:
        list_of_competitions = json.load(comps)['competitions']
        return list_of_competitions


# Initialisation de l'application Flask
app = Flask(__name__)
app.secret_key = 'something_special'

competitions = load_competitions()
clubs = load_clubs()


# Route pour la page d'accueil
@app.route('/')
def index():
    return render_template('index.html')


# Vérification de l'email
def check_email(email: str) -> dict:
    clubs_found = []
    for club in clubs:
        if club['email'] and club['email'] == email:
            clubs_found.append(club)

    if not clubs_found:
        return {}
    else:
        return clubs_found[0]


# Route pour afficher le résumé
@app.route('/showSummary', methods=['POST'])
def show_summary():
    club = check_email(request.form['email'])
    if not club:
        return render_template('index.html', email_error=True)
    else:
        return render_template('welcome.html', club=club, competitions=competitions)


# Route pour effectuer une réservation
@app.route('/book/<competition>/<club>')
def book(competition, club):
    found_club = [c for c in clubs if c['name'] == club][0]
    found_competition = [c for c in competitions if c['name'] == competition][0]
    if found_club and found_competition:
        return render_template('booking.html', club=found_club, competition=found_competition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)


# Route pour acheter des places
@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    places_required = int(request.form['places'])
    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
    flash('Great-booking complete!')
    return render_template('welcome.html', club=club, competitions=competitions)

# TODO: Ajouter une route pour afficher les points


# Route pour la déconnexion
@app.route('/logout')
def logout():
    return redirect(url_for('index'))


# Lancement de l'application
if __name__ == '__main__':
    app.run(debug=True)
