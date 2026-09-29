"""
Intermediate Python Function Examples with Comments
"""

# --------------------------------------------------
# 1. Count Frequency of Each Character
# --------------------------------------------------
def char_frequency(text):
    freq = {}

    # Count each character
    for ch in text:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    return freq

print("1. Character Frequency")
print(char_frequency("banana"))
print()


# --------------------------------------------------
# 2. Find Second Largest Number
# --------------------------------------------------
def second_largest(numbers):

    # Remove duplicates
    unique_numbers = list(set(numbers))

    # Sort numbers
    unique_numbers.sort()

    return unique_numbers[-2]

print("2. Second Largest Number")
print(second_largest([10, 5, 20, 8, 20, 15]))
print()


# --------------------------------------------------
# 3. Count Words in a Sentence
# --------------------------------------------------
def word_count(sentence):

    words = sentence.split()
    result = {}

    for word in words:
        result[word] = result.get(word, 0) + 1

    return result

print("3. Word Count")
print(word_count("python is good python is easy"))
print()


# --------------------------------------------------
# 4. Prime Number Check
# --------------------------------------------------
def is_prime(num):

    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

print("4. Prime Number Check")
print(is_prime(11))
print(is_prime(12))
print()


# --------------------------------------------------
# 5. Find Prime Numbers in a Range
# --------------------------------------------------
def primes_between(start, end):

    primes = []

    for num in range(start, end + 1):

        prime = True

        if num < 2:
            continue

        for i in range(2, num):
            if num % i == 0:
                prime = False
                break

        if prime:
            primes.append(num)

    return primes

print("5. Prime Numbers Between Range")
print(primes_between(1, 20))
print()


# --------------------------------------------------
# 6. Find Duplicate Elements
# --------------------------------------------------
def find_duplicates(numbers):

    seen = set()
    duplicates = set()

    for num in numbers:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)

print("6. Duplicate Elements")
print(find_duplicates([1,2,3,2,4,5,1,6]))
print()


# --------------------------------------------------
# 7. Student Marks Analysis
# --------------------------------------------------
def student_report(marks):

    highest = max(marks.values())
    lowest = min(marks.values())
    average = sum(marks.values()) / len(marks)

    return highest, lowest, average

students = {
    "Rahul": 80,
    "Priya": 95,
    "Amit": 70
}

print("7. Student Report")
print(student_report(students))
print()


# --------------------------------------------------
# 8. Password Strength Checker
# --------------------------------------------------
def password_strength(password):

    if len(password) < 8:
        return "Weak"

    has_digit = False

    for ch in password:
        if ch.isdigit():
            has_digit = True

    if has_digit:
        return "Strong"

    return "Medium"

print("8. Password Strength")
print(password_strength("abc"))
print(password_strength("python123"))
print()


# --------------------------------------------------
# 9. Employee Salary Calculator
# --------------------------------------------------
def calculate_salary(basic):

    hra = basic * 0.20
    da = basic * 0.10

    gross = basic + hra + da

    return gross

print("9. Salary Calculator")
print(calculate_salary(50000))
print()


# --------------------------------------------------
# 10. Library Management Example (OOP)
# --------------------------------------------------
class Library:

    def __init__(self):
        # Store books in a list
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def show_books(self):
        return self.books


lib = Library()

lib.add_book("Python")
lib.add_book("Java")

print("10. Library Management")
print(lib.show_books())

lib.remove_book("Java")

print(lib.show_books())
