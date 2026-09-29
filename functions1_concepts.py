"""
Python Functions Examples
Each example contains comments explaining what it does.
"""

# --------------------------------------------------
# 1. Simple Function
# --------------------------------------------------
def greet():
    print("Hello World")

greet()


# --------------------------------------------------
# 2. Function with Parameters
# --------------------------------------------------
def greet_name(name):
    print("Hello", name)

greet_name("Thunder")


# --------------------------------------------------
# 3. Function Returning a Value
# --------------------------------------------------
def add(a, b):
    return a + b

result = add(10, 20)
print(result)


# --------------------------------------------------
# 4. Function with Default Parameter
# --------------------------------------------------
def greet_default(name="Guest"):
    print("Hello", name)

greet_default()
greet_default("Rahul")


# --------------------------------------------------
# 5. Function with Multiple Parameters
# --------------------------------------------------
def student(name, age, city):
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

student("Rahul", 22, "Delhi")


# --------------------------------------------------
# 6. Function Returning Multiple Values
# --------------------------------------------------
def calculate(a, b):
    return a + b, a - b, a * b

sum_, diff, prod = calculate(10, 5)
print(sum_, diff, prod)


# --------------------------------------------------
# 7. Function Using a List
# --------------------------------------------------
def find_sum(numbers):
    return sum(numbers)

print(find_sum([10, 20, 30, 40]))


# --------------------------------------------------
# 8. Function Using a Dictionary
# --------------------------------------------------
def display_student(student):
    for key, value in student.items():
        print(key, ":", value)

display_student({"name": "Rahul", "age": 22})


# --------------------------------------------------
# 9. Function with *args
# --------------------------------------------------
def add_numbers(*args):
    print("Arguments:", args)
    print("Sum:", sum(args))

add_numbers(10, 20, 30, 40)


# --------------------------------------------------
# 10. Function with **kwargs
# --------------------------------------------------
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

display_info(name="Rahul", age=22, city="Delhi")


# --------------------------------------------------
# 11. Lambda Function
# --------------------------------------------------
square = lambda x: x * x
print(square(5))


# --------------------------------------------------
# 12. Recursive Function
# --------------------------------------------------
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# --------------------------------------------------
# 13. Function with Boolean Return
# --------------------------------------------------
def is_even(num):
    return num % 2 == 0

print(is_even(10))
print(is_even(7))


# --------------------------------------------------
# 14. Function with Exception Handling
# --------------------------------------------------
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(divide(10, 2))
print(divide(10, 0))


# --------------------------------------------------
# 15. Nested Function
# --------------------------------------------------
def outer():
    print("Outer Function")

    def inner():
        print("Inner Function")

    inner()

outer()


# --------------------------------------------------
# 16. Function Using map()
# --------------------------------------------------
def square_func(x):
    return x * x

numbers = [1, 2, 3, 4]
print(list(map(square_func, numbers)))


# --------------------------------------------------
# 17. Function Using filter()
# --------------------------------------------------
def even_check(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
print(list(filter(even_check, numbers)))


# --------------------------------------------------
# 18. Generator Function
# --------------------------------------------------
# Generator Function

def my_generator():
    yield 10
    yield 20
    yield 30

# Create generator object
g = my_generator()

print(next(g))  # 10
print(next(g))  # 20
print(next(g))  # 30



"""
Even Simpler Explanation
yield returns a value.
The function pauses.
When next() is called again, it continues from where it stopped.
"""

def numbers():
    for i in range(1, 6):
        yield i

for num in numbers():
    print(num)