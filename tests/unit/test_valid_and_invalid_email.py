# Importation de la fonction check_email depuis le module 'server'.
from server import check_email


# Test pour vérifier le comportement de la fonction check_email avec un e-mail invalide.
def test_invalid_email():
    invalid_mail = 'invalid@simplylift.co'  # Définition d'un e-mail invalide pour le test.
    club = check_email(invalid_mail)  # Appel de la fonction check_email avec l'e-mail invalide.
    assert not club  # Vérification que la fonction retourne False ou None pour un e-mail invalide.


# Test pour vérifier le comportement de la fonction check_email avec un e-mail valide.
def test_valid_email():
    valid_mail = 'john@simplylift.co'  # Définition d'un e-mail valide pour le test.
    club = check_email(valid_mail)  # Appel de la fonction check_email avec l'e-mail valide.
    # Vérification que la fonction retourne un dictionnaire avec l'e-mail correspondant.
    assert club['email'] == valid_mail
