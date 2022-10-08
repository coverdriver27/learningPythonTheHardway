#  Exercise 16 - Reading and Writing Files

from sys import argv

script, filename = argv

print(f"We are going to erase {filename}.")
print("If you do not want that, hit CTRL+C (^C).")
print("If you do want that hit, RETURN.")

input("> ?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print(f"Now i am going to ask you for three lines to write into {filename}.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print(f"I am now going to write these lines into {filename}.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print(f"\nAnd finally, we close {filename}")
target.close()