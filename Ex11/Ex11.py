#  Exercise 11 - Asking Questions

print("How old are you? ", end='')
age = input()
# print(">>>>> age=", repr(age))  --> We can use the repr function to find out what the pythong representation of
# the variable (Debugging step)

# age = int(input()) --> this only accepts a int value, if else the output will error out
print("How tall are you? ", end='')
height = input()
print("How much do you weigh? ", end='')
weight = input()
# We put a end=' ' at the end of each print line. This tells print to not end the line with a newline character and go
# to the next line.
print(f"\nSo, you're {age} years old, {height} tall and {weight} lbs heavy.")  # f-string that is able to call
# python variables within the print string

# -------------------------------------------------------------------------------------------------------------------

print("\nLets Add Some Numbers.")
print("What is the first number you want to add? ", end='')
num1 = int(input())
print("What is the second number you want to add? ", end='')
num2 = int(input())
addition = num1 + num2
print(f"\nThe sum of the two number is: {addition} ")

# ------------------------------Another way below---------------------------------------------------------------------
# Taking number 1 from user as int
# num1 = int(input("Please Enter First Number: "))

# Taking number 2 from user as int
# num2 = int(input("Please Enter Second Number: "))

# adding num1 and num2 and storing them in
# variable addition
# addition = num1 + num2

# printing
# print("The sum of the two given numbers is {} ".format(addition))

