# Exercise 8 - Printing, Printing

formatter = "{} {} {} {}" # Here we are setting the formatter variable to take 4 arguments and
# print it in one single line

print(formatter.format(1, 2, 3, 4)) # here we are calling the formatter variable and passing 4 intergers to print
print(formatter.format("One", "Two", "Three", "Four")) # Here we are calling the formatter
# variable and passing 4 Strings
print(formatter.format(True, False, True, False)) # Here we are passing 4 boolean values
print(formatter.format(formatter, formatter, formatter, formatter)) # Here were are just printing formatter 4 times
# below if we forget a comma seperator it would pass only 3 strings which would cause errors
# This is a good place to debug test
# lines = (
#     "Try Your",
#     "Own Text Here",
#     "Maybe a Poem?",
#     "Or a song about fear"
# )
# print(">>>>>> lines", lines)
# or
# print(">>>>>> lines", repr(lines)) --> repr is the representation python has, this we can visually see
# the strings broken down with commas
print(formatter.format(
    "Try Your",
    "Own Text Here",
    "Maybe a Poem?",
    "Or a song about fear"
)) # Here we are basically passing 4 Strings to the formatter variable to be printed in the {0} {1} {2} {3} format

# If we try to pass more than 4 values to {} {} {} {}, The value/Argument after the 4th would not be printed

formatter2 = "{}    {}    {}     {}"

print(formatter2.format(1, 2, 3, 4, 5, 6))  # here after the 4th passed value everything else would not be printed
# will also be spaced appropriatly on how we set it in formatter2