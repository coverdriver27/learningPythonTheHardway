# Exercise 18 - Names, Variables, Code, Functions

# This one is like your scripts with argv

# Writing various functions that take x number of arguments to run to do things later on

# using '*args' we assign multiple arguments for the function to take
# def is used to define a function and after the colon ":" lines after will be indented to do things what the function
# is meant to do
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# Ok, that *args is actually pointless, we can just do this (Not really pointless if you are unsure of how many
# arguments you want to assign
# The following function takes two arguments
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# This just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# This one takes no arguments
def print_none():
    print("I got nothing.")

# testing
def adding_calculator(arg1, arg2):
    number1 = int(arg1)
    number2 = int(arg2)
    add = number1 + number2
    print(f"The sum of the two numbers is: {add}")

# def input_adding(arg1, arg2):
#     input("Hi!!!")

# Here we are calling the functions we created above and running it passing arguments within the ()
print_two("John","Snow")
print_two_again("John","Snow")
print_one("John Snow")
print_none()
adding_calculator(20, 30)
# input_adding("lol","ol")
# all of these functions have a print command within each function, that is why when you run this code it prints
# out things
