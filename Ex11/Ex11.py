#  Exercise 11 - Asking Questions

print("How old are you?", end='')
age = input()
# print(">>>>> age=", repr(age))  --> We can use the repr function to find out what the pythong representation of
# the variable (Debugging step)

# age = int(input()) --> this only accepts a int value, if else the output will error out
print("How tall are you?", end='')
height = input()
print("How much do you weigh?", end='')
weight = input()
# We put a end=' ' at the end of each print line. This tells print to not end the line with a newline character and go
# to the next line.
print(f"So, you're {age} years old, {height} tall and {weight} lbs heavy.")  # f-string that is able to call
# python variables within the print string
