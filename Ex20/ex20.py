# Exercise 20 - Functions and Files

from sys import argv  # From sys module we are importing the argv feature/function

script, input_file = argv  # Passing two parameter variables to the argument vector

# We are creating a function called print_all that prints the file via the .read function
# f is reference to the current file variable down below
def print_all(f):
    print(f.read())

# Same thing as above, but here we are performing a .seek function
def rewind(f):
    f.seek(0)

# this function is to print a current line with counting lines. line_count we are setting it in a way that
# prints numbers per line. the .readline takes one line and prints it out
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)  # setting current file variable to open the input_file

print("First let's print the whole file:\n")  # print statement

print_all(current_file)  # running the print_all function and passing current_file as the parameter in reference
# to "f" above

print("Now let's rewind, kind of like a tape.\n")

rewind(current_file)  # we are using the rewind function

print("let's print three lines:\n")

current_line = 1
print_a_line(current_line, current_file)

# current_line = current_line + 1
current_line += 1  # Using the += as a counter
print_a_line(current_line, current_file)

# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)
print()
