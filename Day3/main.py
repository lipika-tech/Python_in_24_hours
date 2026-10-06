from validators import validate_phone, validate_email, validate_marks

tests = [
    (validate_phone, "9876543210"),
    (validate_phone, "12345"),
    (validate_email, "Asha@Example.com"),
    (validate_email, "asha.example.com"),
    (validate_marks, "88"),
    (validate_marks, "150"),
    (validate_marks, "abc"),
]

for func, value in tests:
    try:
        result = func(value)
    except ValueError as e:
        print(f"INVALID  {func.__name__}: {e}")
    else:
        print(f"OK       {func.__name__}: {result}")
