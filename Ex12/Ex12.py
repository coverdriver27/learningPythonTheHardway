
# Exercise 12 - Prompting People

# Same as Exercise 11, but in this EX: We are compressing the input into one line

age = input("How old are you? ")  # we need to know the users age, so we make a variable called age and print a string
# that prompts the user for their age
height = input("How tall are you? ")  # Prompting the user for height
weight = input("how much do you weight? ")  # Prompting the user for their weight

print(f"\nSo, you are {age} years old, {height} inches tall and {weight} lbs heavy.")
# Using a f-string, we print a statement with calling the values from the users inputs
#  -----------------------------------------------------------------------------------------------

# Addition calculator
a = "Enter a number: "
b = "Enter a second number: "

number1 = int(input(f"\n{a}"))  # For this variable the input can only be a int, also this input prompt is
# using a f-string within the function
number2 = int(input(f"{b}"))
add = number1 + number2

print(f"\nSo the answer is: {add}")
