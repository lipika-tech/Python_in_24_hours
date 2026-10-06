"""validators.py - Example 3: a module that raises exceptions (links to Part 3)."""


def validate_phone(phone):
    """Indian mobile number: 10 digits, starting with 6-9."""
    phone = phone.strip()
    if not phone.isdigit():
        raise ValueError(f"'{phone}' must contain digits only")
    if len(phone) != 10:
        raise ValueError(f"'{phone}' must have 10 digits")
    if phone[0] not in "6789":
        raise ValueError(f"'{phone}' must start with 6, 7, 8 or 9")
    return phone


def validate_email(email):
    email = email.strip()
    if email.count("@") != 1 or "." not in email.split("@")[1]:
        raise ValueError(f"'{email}' is not a valid email")
    return email.lower()


def validate_marks(marks):
    marks = int(marks)          # may raise ValueError for "abc"
    if not 0 <= marks <= 100:
        raise ValueError(f"marks {marks} must be between 0 and 100")
    return marks
