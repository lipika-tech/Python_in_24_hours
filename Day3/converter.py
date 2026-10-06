"""converter.py - Example 2: a module with its own test block."""

USD_RATE = 83.0   # 1 USD in INR (sample value)


def celsius_to_fahrenheit(c):
    return round(c * 9 / 5 + 32, 1)


def km_to_miles(km):
    return round(km * 0.621371, 2)


def inr_to_usd(rupees):
    return round(rupees / USD_RATE, 2)


if __name__ == "__main__":
    # Runs ONLY with: python converter.py
    print("Self-test of converter.py")
    print(celsius_to_fahrenheit(100))   # 212.0
    print(km_to_miles(10))              # 6.21
    print(inr_to_usd(8300))             # 100.0
