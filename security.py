import bcrypt


def hash_password(password: str) -> str:
    # Convert password to bytes
    password_bytes = password.encode("utf-8")

    # Hash the password
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    # Store as string in database
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )