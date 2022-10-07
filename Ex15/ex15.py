# Exercise 15 - Reading Files

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here is Your file {filename}: ")
print(txt.read())

print("Type the filename again: ")
file_again = input("\n> ")

txt_again = open(file_again)

print(txt_again.read())
