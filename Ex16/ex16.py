#  Exercise 16 - Reading and Writing Files

from sys import argv  # from the module sys we are importing the argv feature/function

script, filename = argv  # Passing two variable parameters

print(f"We are going to erase {filename}.")  # a f-string that is able to call and print one of the filename variable
print("If you do not want that, hit CTRL+C (^C).")  # Just a printing of a string
print("If you do want that hit, RETURN.")  # printing

input("> ?")  # prompting a input here with a string, we can type anything here but once we press enter it moves to the
# next line of code to be executed

print("Opening the file...")  # Printing a string here
target = open(filename, 'w')  # The target variable is set to the open() function, and within the file opening function
# we are passing two parameters. one is the file to be opened, and the other 'w' means open the file with WRITE access.

print("Truncating the file. Goodbye!")  # Printing a string
target.truncate()  # Truncate function deletes the contents of a file, so here the target variable is already set to a
# file from line 15, basically we are saying target(Variable).(Do Something)--> truncate()

print(f"Now i am going to ask you for three lines to write into {filename}.")  # Printing a f-string

line1 = input("line 1: ")  # Prompting the user for input and saving it on a variable called line1
line2 = input("line 2: ")  # Prompting the user for input and saving it on a variable called line2
line3 = input("line 3: ")  # Prompting the user for input and saving it on a variable called line3

print(f"I am now going to write these lines into {filename}.")  # Printing a f-string

# Now we are going to write things to the file that we opened on line 15
# target variable is already set to the opened file
# target.write(line1)  # calling the target variable that has the file open, (.) is to do something --> write() function
# to write things to the file and within the parameter () we add what we want to write
# target.write("\n")  # Same thing above but here we are just writing a new line
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write(f"{line1}\n{line2}\n{line3}")

print(f"\nAnd finally, we close {filename}")  # printing a f-string
target.close()  # We are closing the opened and written file

openfile = open(filename)
# now lets read the file you just created
print(f"\nNow lets see what you wrote into {filename}. \n")
print(openfile.read())  # This will print what you wrote into the file earlier via the read function

