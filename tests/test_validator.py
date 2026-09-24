from emailintel.core.validator import validate_email


def test_valid_gmail():
    result = validate_email("User.Name+tag@gmail.com")
    assert result.valid
    assert result.profile is not None
    assert result.profile.domain == "gmail.com"
    assert result.profile.is_free_mail is True


def test_invalid_email():
    assert not validate_email("not-an-email").valid


def test_role_account():
    result = validate_email("security@example.com")
    assert result.valid and result.profile and result.profile.is_role_based
