from server import check_email


def test_invalid_email():
    invalid_mail = 'invalid@simplylift.co'
    club = check_email(invalid_mail)
    assert not club


def test_valid_email():
    valid_mail = 'john@simplylift.co'
    club = check_email(valid_mail)
    assert club['email'] == valid_mail
