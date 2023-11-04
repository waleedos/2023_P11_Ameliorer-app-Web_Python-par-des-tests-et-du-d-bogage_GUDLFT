# test_fonctionnel_full.py #

# Importations nécessaires pour les tests
from server import app  # Importe l'instance de l'application Flask
import pytest  # Importe le framework de test pytest
from server import check_date_validity, update_places  # Importe des fonctions spécifiques pour les tests


# Définition d'un "fixture" pytest pour créer un client de test.
# Ce client sera utilisé pour faire des requêtes vers notre application Flask dans un contexte de test.
@pytest.fixture
def client():
    app.config['TESTING'] = True  # Active le mode test sur l'application Flask
    with app.test_client() as client:  # Ouvre un contexte avec le client de test
        yield client  # Rend le client de test disponible aux fonctions de test


# ******************** TEST DE LOGIN ********************#

# Fonction de test pour vérifier si le login est effectué avec succès
def test_valid_login(client):
    # Fait une requête POST vers '/showSummary' avec un email valide et vérifie si le mot 'Welcome' est présent
    # dans la réponse.
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})  # Envoie la requête avec
    # les données de l'email
    assert b'Welcome' in response.data  # Vérifie que la réponse contient le mot 'Welcome' (b signifie bytes
    # en Python)


# ******************** TEST DE NAVIGATION ********************#

# Fonction de test pour vérifier la navigation dans l'application
def test_navigation(client):
    # Premièrement, connecte l'utilisateur avec un email valide
    client.post('/showSummary', data={'email': 'john@simplylift.co'})  # Fait une requête POST pour se connecter

    # Ensuite, teste la navigation vers la table des clubs et vérifie que le code de réponse est 200 (OK)
    response = client.get('/club_table.html')  # Fait une requête GET vers la table des clubs
    assert response.status_code == 200  # Vérifie que le statut de la réponse est 200, ce qui indique le succès
    # de la requête

    # Teste ensuite la déconnexion en naviguant vers la page '/logout'
    response = client.get('/logout')  # Fait une requête GET pour se déconnecter
    assert response.status_code == 302  # Vérifie que le statut de la réponse est 302, ce qui indique une redirection


# ******************** TEST DE RÉSERVATION ********************#

# Fonction de test pour vérifier le processus de réservation
def test_booking(client):
    # Étape 1 : Connexion avec un email valide
    client.post('/showSummary', data={'email': 'john@simplylift.co'})  # Se connecte avec un email valide

    # Étape 2 : Navigation vers la page de réservation pour un événement et un club donnés
    response = client.get('/book/Spring Festival/Simply Lift')  # Fait une requête GET pour la page de réservation
    assert response.status_code == 200  # Vérifie que le code de réponse est 200 (OK), indiquant que la page est
    # accessible

    # Étape 3 : Finalisation de la réservation en envoyant les détails nécessaires via une requête POST
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',  # Nom du club effectuant la réservation
        'competition': 'Spring Festival',  # Nom de la compétition pour laquelle la réservation est faite
        'places': '5'  # Nombre de places à réserver
    })
    # Vérifie que la réponse contient la phrase 'Great-booking complete!', signifiant que la réservation a été
    # effectuée avec succès
    assert b'Great-booking complete!' in response.data


# ************** TEST DE VÉRIFICATION DE L'EMAIL *******************#

# Fonction de test pour vérifier la gestion d'un email invalide lors de la connexion
def test_invalid_email(client):
    # Fait une requête POST avec un email invalide pour tester la réponse du serveur
    response = client.post('/showSummary', data={'email': 'invalid@simplylift.co'})
    # Vérifie que la réponse contient un message d'erreur indiquant que l'email n'a pas été trouvé
    assert b'Sorry, that email wasn\'t found.' in response.data


# Fonction de test pour vérifier la gestion d'un email valide lors de la connexion
def test_valid_email(client):
    # Fait une requête POST avec un email valide pour tester la réponse du serveur
    response = client.post('/showSummary', data={'email': 'john@simplylift.co'})
    # Vérifie que la réponse contient un message de bienvenue personnalisé avec l'email de l'utilisateur
    assert b'Welcome, john@simplylift.co' in response.data


# ******** TEST DE VALIDITÉ DE LA DATE DE LA COMPÉTITION ********#

# Fonction de test pour vérifier la validité de la date d'une compétition
def test_invalid_competition_date(client):
    # Crée un dictionnaire représentant une compétition avec une date passée
    competition = {'date': '2020-01-01 10:00:00'}
    # Vérifie que la fonction check_date_validity retourne False pour une date passée
    assert not check_date_validity(competition)


# ********* TEST DE MISE À JOUR DES POINTS ET DES PLACES *********#

# Fonction de test pour vérifier la mise à jour des points et des places disponibles
def test_update_points_and_places(client):
    # Crée des dictionnaires représentant une compétition et un club
    competition = {'numberOfPlaces': '10'}
    club = {'points': '15'}
    # Définit le nombre de places requises pour la réservation
    places_required = 5
    # Vérifie que la fonction update_places effectue correctement la mise à jour
    assert update_places(competition, places_required, club)


# *********** Test de la limite de points du club **************#

# Fonction de test pour vérifier que la limite de points d'un club est respectée lors d'une réservation
def test_club_point_limit(client):
    # Étape 1 : Connexion avec un email valide existant dans le fichier clubs.json
    client.post('/showSummary', data={'email': 'john@simplylift.co'})

    # Étape 2 : Tente de réserver un nombre de places excédant les points disponibles du club
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': '20'  # Un nombre hypothétique supérieur aux points disponibles du club
    })
    # Vérifie que la réponse contient un message d'erreur indiquant que le nombre de places demandé est invalide
    assert b'You tried to book an invalid number of places, sorry' in response.data


# ******** Test de la disponibilité des places dans une compétition ************#

# Fonction de test pour vérifier la gestion de la disponibilité des places pour une compétition
def test_competition_availability(client):
    # Étape 1 : Connexion avec un email valide pour simuler un utilisateur connecté
    client.post('/showSummary', data={'email': 'john@simplylift.co'})

    # Étape 2 : Tentative de réservation pour une compétition qui est censée être complète (sans places disponibles)
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Fully Booked Competition',  # Nom hypothétique d'une compétition sans places disponibles
        'places': '1'  # Tentative de réservation d'une place
    }, follow_redirects=True)

    print(response.status_code)  # Affichage du code de statut pour le débogage
    # Assertion pour s'assurer que la réponse contient un message d'erreur spécifique lié au nombre de places
    assert b'You tried to book an invalid number of places, sorry' in response.data


# ******** Test de la navigation sans connexion ********#

# Fonction de test pour vérifier l'accès à certaines pages sans être connecté
def test_access_without_login(client):
    # Test d'accès à la page club_table.html sans connexion préalable
    response = client.get('/club_table.html')
    # L'assertion vérifie que la page est accessible et renvoie un code de statut HTTP 200 OK
    assert response.status_code == 200

    # Test d'accès à la page welcome.html sans connexion préalable
    response = client.get('/showSummary')
    # L'assertion vérifie que l'accès est refusé ou redirigé, renvoyant un code de statut HTTP 405 Method Not Allowed
    assert response.status_code == 405

    # Test d'accès à la page booking.html sans connexion préalable
    response = client.get('/book/Spring Festival/Simply Lift')
    # L'assertion vérifie que la page est accessible et renvoie un code de statut HTTP 200 OK
    assert response.status_code == 200


# ******** Tests des messages flash ********#

# Fonction de test pour vérifier l'affichage des messages flash en réponse à certaines actions
def test_flash_messages(client):
    # Test de l'affichage d'un message d'erreur lors de la connexion avec un email invalide
    response = client.post('/showSummary', data={'email': 'invalide@email.com'}, follow_redirects=True)
    # Assertion pour vérifier que le message d'erreur s'affiche correctement dans la réponse
    assert b"Sorry, that email wasn't found." in response.data

    # Test de l'affichage d'un message d'erreur lors d'une tentative de réservation invalide
    client.post('/showSummary', data={'email': 'john@simplylift.co'})
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': '100'  # Un nombre de places invalide
    }, follow_redirects=True)
    # Assertion pour vérifier que le message d'erreur s'affiche correctement dans la réponse
    assert b'You tried to book an invalid number of places, sorry' in response.data

    # Test de l'affichage d'un message de réussite lors d'une réservation réussie
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': '1'  # Un nombre de places valide
    }, follow_redirects=True)
    # Assertion pour vérifier que le message de réussite s'affiche correctement dans la réponse
    assert b'Great-booking complete!' in response.data

    # Test de l'affichage d'un message lors de la tentative de réservation pour une compétition passée
    existing_competition = 'Spring Festival'  # Remplacer par le nom réel d'une compétition passée si nécessaire
    response = client.get(f'/book/{existing_competition}/Simply Lift', follow_redirects=True)
    # Assertion à définir en fonction du message réel attendu pour une compétition passée
    assert b'Selected competition is over' in response.data  # Remplacer par le message flash réel


# ******** Test fonctionnel de la validité des données du formulaire ************#

# Cette fonction de test est conçue pour vérifier la validité des données du formulaire lors d'une
# réservation de places.
def test_form_data_validity(client):
    # Connexion en utilisant un email valide pour simuler un utilisateur connecté.
    client.post('/showSummary', data={'email': 'john@simplylift.co'})

    # Test avec un nombre de places négatif pour simuler une saisie de formulaire incorrecte.
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': '-1'  # Nombre de places négatif, ce qui est invalide.
    }, follow_redirects=True)
    # L'assertion vérifie que la réponse contient un message d'erreur approprié pour une saisie de
    # nombre de places négatif.
    assert b'You tried to book an invalid number of places, sorry' in response.data

    # Test avec zéro place pour simuler une saisie de formulaire incorrecte.
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': '0'  # Zéro place, ce qui est une saisie invalide.
    }, follow_redirects=True)
    # L'assertion vérifie que la réponse contient un message d'erreur approprié pour une saisie de zéro place.
    assert b'You tried to book an invalid number of places, sorry' in response.data

    # Test avec un nombre de places supérieur aux points disponibles pour simuler une saisie de formulaire incorrecte.
    response = client.post('/purchasePlaces', data={
        'club': 'Simply Lift',
        'competition': 'Spring Festival',
        'places': '100'  # Nombre de places supérieur aux points disponibles, ce qui est invalide.
    }, follow_redirects=True)
    # L'assertion vérifie que la réponse contient un message d'erreur approprié pour une saisie de
    # nombre de places trop élevé.
    assert b'You tried to book an invalid number of places, sorry' in response.data

    # Test avec un nombre de places sous forme de texte pour simuler une saisie de formulaire incorrecte.
    with pytest.raises(ValueError):  # On s'attend à une erreur de type ValueError lors de la tentative de réservation.
        response = client.post('/purchasePlaces', data={
            'club': 'Simply Lift',
            'competition': 'Spring Festival',
            'places': 'texte'  # Saisie de texte au lieu d'un nombre, ce qui est invalide.
        }, follow_redirects=True)
