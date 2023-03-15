# Is it possible to use a class like it's an object?

# One way to use a class like an object is to assign it to a variable. For example, suppose you have a class called


class MyClass:
    def my_method(self):
        print("Hello, world!")

my_class = MyClass

my_instance = my_class()
my_instance.my_method()  # prints "Hello, world!"

# Do you think there's such thing as an "is-many" relationship? Read about "multiple inheritance,"

"""
Multiple inheritance is a feature in object-oriented programming languages that allows a class to inherit from multiple 
parent classes. This means that a single class can have multiple "is-a" relationships with different classes.

For example, suppose you have a class called Bird that represents all birds, and a class called Mammal that represents 
all mammals. You can create a class called Platypus that inherits from both Bird and Mammal, like this:
"""

class Bird:
    def fly(self):
        print("I can fly!")

class Mammal:
    def feed_young(self):
        print("I feed my young with milk.")

class Platypus(Bird, Mammal):
    pass

