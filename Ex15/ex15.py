# Exercise 15 - Reading Files

from sys import argv  # from the module sys, import the function or parameter argv

script, filename = argv  # Passing two (1) parameters to argv

txt = open(filename)  # here we are using the open() function to open a text file and store the contents
# of it in a variable

print(f"Here is Your file {filename}: ")  # using a f-string to print out the filename variable
print(txt.read())  # printing the txt variable from above that uses "." that tells python to do something,
# here we use the read() method for reading the content of the file

#  below is the same from above but, it is a different approach, that prompts the user to enter the file name
print("Type the filename again: ")
file_again = input("\n> ")  # Prompts the user for a filename, and that input is saved in the file_again variable

txt_again = open(file_again)  # Now we use the file_again variable value within the open() function to open the contents
# of the provided txt file

print(txt_again.read())  # printing the txt variable from above that uses "." that tells python to do something,
# here we use the read() method for reading the content of the file and print it out
txt_again.close()  # closing the opened file
txt.close()

