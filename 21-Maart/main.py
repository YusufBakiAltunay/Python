#Functions and Modules

def greet():
    print("Hello!")

greet()  # Output: Hello!


def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Anka")  # Output: Hello, Anka!


def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8


def welcome(name="guest"):
    print(f"Welcome, {name}!")

welcome()          # Output: Welcome, guest!
welcome("Anka")    # Output: Welcome, Anka!


# import math

# print(math.sqrt(16))  # Output: 4.0


# from math import pi, sqrt

# print(pi)        # 3.141592...
# print(sqrt(9))   # 3.0