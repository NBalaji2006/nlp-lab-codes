"""Validate a password against the lab's five security requirements."""
import re


def validate_password(password: str) -> tuple[bool, list[str]]:
    errors = []
    if len(password) < 8:
        errors.append("Use at least 8 characters.")
    if not re.search(r"[A-Z]", password):
        errors.append("Include at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        errors.append("Include at least one lowercase letter.")
    if not re.search(r"\d", password):
        errors.append("Include at least one digit.")
    if not re.search(r"[@#$%&*]", password):
        errors.append("Include at least one special character from @ # $ % & *.")
    return not errors, errors


def main() -> None:
    password = input("Enter password: ")
    valid, errors = validate_password(password)
    if valid:
        print("Password is valid.")
    else:
        print("Password is not valid:")
        print("\n".join(f"- {error}" for error in errors))


if __name__ == "__main__":
    main()
