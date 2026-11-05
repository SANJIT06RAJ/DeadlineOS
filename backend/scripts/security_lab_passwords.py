"""Isolated security lab: password hashing with Argon2id."""

from getpass import getpass

from argon2 import PasswordHasher
from argon2.exceptions import (
    InvalidHashError,
    VerificationError,
    VerifyMismatchError,
)

# Argon2id is the default variant used by PasswordHasher.
password_hasher = PasswordHasher()


def hash_password(password: str) -> str:
    """Hash a password. Never store the original password."""
    if not password:
        raise ValueError("Password cannot be empty.")

    return password_hasher.hash(password)


def verify_password(password: str, stored_hash: str) -> bool:
    """Verify a password against its stored Argon2 hash."""
    try:
        return password_hasher.verify(stored_hash, password)
    except (VerifyMismatchError, VerificationError, InvalidHashError):
        return False


def main() -> None:
    print("=== Argon2id Password Security Lab ===")

    password = getpass("Enter a test password: ")
    stored_hash = hash_password(password)

    print("\nPassword hashed successfully.")
    print("Stored hash:", stored_hash)

    correct = verify_password(password, stored_hash)
    print("Correct password accepted:", correct)

    incorrect = verify_password("DefinitelyWrongPassword123!", stored_hash)
    print("Incorrect password rejected:", not incorrect)


if __name__ == "__main__":
    main()
