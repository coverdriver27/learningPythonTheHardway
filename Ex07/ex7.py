# Exercise 7 - More Printing

# using .format stuff

print("Mary had a little lamb.")  # Regular Print Statement
# a = "Snow"
# print(f"Its fleece was white as {a}")  # Testing to get the same prints as the {} --> .format() Statement below
# print(f"Its fleece was white as {'Snow'}")
print("Its fleece was white in {}.".format("Snow")) # Here without using the f string the pass in a value to the print
# statement, we are using a regular print statement with a curly bracket and after the "" we are using .format() and
# Within the paranthesis we are passing a value to pass into the curly braces for the print statement
print("And everywhere that mary went.") # Regular print statement
print("-" * 10) # What that do? >>>> We multiplied one character to print by 10 times

end1 = "C" # Assigning letters/characters to variables
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "y"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6, end=' ') # Over here we want to print the statement in line 28 and 34
# Togather, so after the last variable being printed we use , end=' ' as a place holder and a space between so python
# can print the next line after end=' '

# One mistake i did in the above line was, after typing + end6, rather than the comma i added a + end=' ' which does
# not work
print(end7 + end8 + end9 + end10 + end11 + end12, end=' - Double Beef with extra cheese') # here we are using
# this end=' ' and adding a string inside it to print
