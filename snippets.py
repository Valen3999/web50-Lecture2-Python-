1. Hello World & Variables


# Hello World
print("Hello, world!")

# Variable assignment
a = 28           # int
b = 1.5          # float
c = "Hello!"     # string
d = True         # boolean
e = None         # NoneType

2. User Input & String Formatting


# Basic input
name = input("Enter your name: ")
print("Hello, " + name)

# Using f-strings for string formatting
print(f"Hello, {name}")

3. Conditions


# If-else condition
num = int(input("Enter a number: "))

if num > 0:
    print("Number is positive")
elif num < 0:
    print("Number is negative")
else:
    print("Number is zero")

    
4. Sequences

Strings
# Accessing string characters
name = "Harry"
print(name[0])  # Output: H
print(name[1])  # Output: a
Lists


# Creating and manipulating lists
names = ["Harry", "Ron", "Hermione"]
print(names)        # Output: ['Harry', 'Ron', 'Hermione']
print(names[1])     # Output: Ron

names.append("Draco")
names.sort()
print(names)        # Output: ['Draco', 'Harry', 'Hermione', 'Ron']
Tuples


# Immutable ordered collection
point = (12.5, 10.6)
print(point[0])  # Output: 12.5
Sets


# Creating and manipulating sets
s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)  # Duplicates won't be added
s.remove(2)

print(s)  # Output: {1, 3, 4}
print(f"The set has {len(s)} elements.")
Dictionaries


# Key-value pairs in a dictionary
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}

# Accessing and modifying dictionary values
print(houses["Harry"])  # Output: Gryffindor
houses["Hermione"] = "Gryffindor"
print(houses["Hermione"])  # Output: Gryffindor
5. Loops
For Loop (list and range)


# Iterate over a list
for name in ["Harry", "Ron", "Hermione"]:
    print(name)

# Using range() to iterate over a sequence of numbers
for i in range(6):
    print(i)
6. Functions


# Defining a function
def greet(name):
    return f"Hello, {name}"

# Calling a function
print(greet("Alice"))  # Output: Hello, Alice
7. Modules


# Importing a module
import math

# Using a function from the math module
print(math.sqrt(16))  # Output: 4.0
8. Object-Oriented Programming


# Defining a class
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"

# Creating an object
dog1 = Dog("Buddy", "Golden Retriever")
print(dog1.bark())  # Output: Buddy says woof!

9. Lambda Functions


# Anonymous functions using lambda
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Lambda inside sort
points = [(2, 5), (1, 2), (4, 4)]
points.sort(key=lambda point: point[1])
print(points)  # Output: [(1, 2), (4, 4), (2, 5)]
10. Decorators


# Simple decorator example
def decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before the function
# Hello!
# After the function
11. Exceptions


# Try-except for error handling
try:
    x = int(input("Enter a number: "))
    print(f"The number is {x}")
except ValueError:
    print("That's not a valid number!")

"""These snippets provide a solid foundation and reference for essential python concepts like working with variables, 
data structures, conditions, loops, functions, object-oriented programming, decorators, and exceptions. You can copy 
these into a GitHub repo and expand them as you encounter more advanced topics in ."""