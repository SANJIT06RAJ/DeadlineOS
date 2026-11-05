import pytest

from scripts.security_lab_passwords import hash_password, verify_password


def test_password_is_hashed():
    password = "TestPassword123!"

    hashed = hash_password(password)

    assert hashed != password
    assert hashed.startswith("$argon2id$")


def test_correct_password_is_accepted():
    password = "TestPassword123!"
    hashed = hash_password(password)

    assert verify_password(password, hashed) is True


def test_incorrect_password_is_rejected():
    hashed = hash_password("TestPassword123!")

    assert verify_password("WrongPassword123!", hashed) is False


def test_same_password_generates_different_hashes():
    password = "TestPassword123!"

    first_hash = hash_password(password)
    second_hash = hash_password(password)

    assert first_hash != second_hash
    assert verify_password(password, first_hash) is True
    assert verify_password(password, second_hash) is True


def test_empty_password_is_rejected():
    with pytest.raises(ValueError, match="Password cannot be empty"):
        hash_password("")


def test_invalid_stored_hash_is_rejected():
    assert verify_password("TestPassword123!", "invalid-hash") is False
