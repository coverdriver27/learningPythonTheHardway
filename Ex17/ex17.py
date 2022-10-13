# Exercise 17 - More Files

from sys import argv  # From sys module we import the argv function/feature
from os.path import exists  # From os.path module we import the exists feature

script, from_file, to_file = argv  # we are passing 3 variables to argv

print(f"Copying from {from_file} To {to_file}")  # f-string that prints out the variables we passed to argv

# We could do these two on one line, how?
# in_data = open(from_file).read() ?

# This is the one-liner code i am using that is different from the book
with open(from_file) as in_file:
    in_data = in_file.read()

# Below is the code from book
# in_file = open(from_file)  # We open a file
# in_data = in_file.read()  # we read the opened file to a variable

print(f"The input of this file is {len(in_data)} bytes long.")  # f-string that prints out a the length os the file in
# (bytes), 'len' is a builtin python function.

print(f"Does the output of this file exist? {exists(to_file)}")  # from the imported feature of 'exists' in above, we
# use it here to check if the file or something exists.
print("Ready, hit enter/return to continue, CTRL+C to abort.")
input("> ?")


# This is the one liner code i am writing that is different from the book

with open(to_file, 'w') as out_file:
    out_file.write(in_data)

# below is the code from book

# out_file = open(to_file, 'w')  # since we want to write the contents of the 1st file to the next file, we open this
# next file with 'w' - write permissions

# out_file.write(in_data)  # in_data is the variable we stored the contents from the first file and we write that
# contents to this second file

print("\nAlright, All done!!!\n")
out_file.close()  # Closing out the opened files
in_file.close()

