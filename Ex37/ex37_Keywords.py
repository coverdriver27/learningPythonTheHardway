# Import statements
import math


# Class definition
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius


# Function definition with lambda
double = lambda x: x * 2

# Try-except block with assert and raise
try:
    x = int(input("Enter a number: "))
    assert x >= 0, "Number must be non-negative"
    print(f"The double of {x} is {double(x)}")
except ValueError:
    print("Invalid input")
except AssertionError as error:
    print(error)
    raise

# For loop with continue and break
for i in range(10):
    if i % 2 == 0:
        continue
    elif i == 7:
        break
    print(i)

# While loop with else
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Loop finished")

# With statement
with open("example.txt", "w") as f:
    f.write("Hello, world!")

# Del statement
x = [1, 2, 3]
del x[0]
print(x)

# Global variable
y = 10


def add_to_y(z):
    global y
    y += z


add_to_y(5)
print(y)

"""
This program defines a Circle class that calculates the area and circumference of a circle, defines a double function 
using a lambda expression, and uses a try-except block to catch exceptions and raise an error if the input number is 
negative. It also includes a for loop that uses continue and break statements, a while loop with an else statement, and 
a with statement for file handling. The del statement is used to delete an item from a list, and the global keyword is 
used to modify a global variable within a function.
"""