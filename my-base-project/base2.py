# Some utility functions
import re

def validate_email(email):
    """Checks if a string is a valid email."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

def format_name(first, last):
    """Formats a name."""
    return f"{last.upper()}, {first.capitalize()}"