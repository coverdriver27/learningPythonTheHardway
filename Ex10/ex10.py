tabby_cat = "\tI'm tabbed in."  # Here we are assigning a string to the variable with a horizontal tab
persian_cat = "I'm split\non a line."  # Assigning a string to the variable and in-between the assigned string we are
# adding a \n to spilit the string and the rest of the string to be printed on the next line
backslash_cat = "I'm \\ a \\ cat."
# backslash_cat1 = "I'm \ a \ cat." --> Same output as above but in this the single \ character is printed out
# as a string

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""  # The addition of """ """ allows us to add multiple lines of strings to be printed on multiple lines

testing_escape = """Checking the \\ Backlash \\ Out
\'This is using Single Quotes\'
\"And this is using double\" 
And if we use \asomething happens --> Adds a ASCII Bell 
What if we add \bsupposed to backspace
Also if we test out \rsomething happens again --> Anything before the the slash r is deleted
If we use \vThis vertically tabs (Nothing happened lol.)
"""

# qoute_testing = '''
# This works too?
# testing this "shoot"
# \t*1
# \t*2
# \t*3\n\t*4
# '''


print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(testing_escape)
# print(backslash_cat1)
# print(qoute_testing)