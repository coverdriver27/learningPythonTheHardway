
days = "Mon Tue Wed Thu Fri Sat Sun"  # for the variable days we are setting a string value with spaces
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"  # For the months variable we are setting a string value, once it hits
# \n the next string values moves to the next line
# months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug" --> if we set this to months the output is more clean
# print(days)
# print(months)

print("Here are the days: ", days)  # Here we are printing a string and printing a variable after
print("Here are the months: ", months)

# Here With the triple (three double-quotes). Will be able to type as much as we like printing in new lines
# all the lines can be encapsulated and printed in line by line format using """xyz"""
print("""
There is something going on here.
With the triple (three double-quotes).
Will be able to type as much as we like
ever 4 lines if we want
Maybe 5? 
or 6.  
""")

# This won't work below as the top code because --> When we use single quotes, every line after the current line
# would need its own quote
# print("There is something going on here.
# With the triple (three double-quotes).
# Will be able to type as much as we like
# ever 4 lines if we want
# Maybe 5?
# or 6.  ")
