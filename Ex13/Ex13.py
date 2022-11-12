# Exercise 13 - Parameter,Unpacking,Variables

from sys import argv  # from the sys system module import feature argument vector or argument variable
# Read the WYSS section for a how to on this
script, first, second, third = argv  # from argv we are going to get 4 variables (Only need 3)
# historical convention we get the name of the script as script variable
# What is argv ?
print(">>> argv=", repr(argv))  # ---> takes arguments (Strings) off a commandline and puts them into a list
print("The script is called: ", script)  # this argument gets mapped to the script variable, is the name of the script
print("Your first variable is: ", first)  # This argument gets mapped to the first variable
print("Your second variable is: ", second)  # Same as above
print("Your Third variable is: ", third)  # Same as above


# Above file can only be run via command line
# If run via IDE, we get a error of --> ValueError: not enough values to unpack (expected 4, got 1)
# Since running this file via command line, we need to add in the script we are running so that value is taken and
# mapped to the executed script
# This python explicitly requires 3 variables to run, if we dont give it 3 variables at the time of running
# it we would get a error --> ValueError: not enough values to unpack (expected 4, got 1)

# ------------------------------------------------------------------------------------------------------------------
# Output
# PS C:Ex13> python Ex13.py apple orange yellow
# >>> argv= ['Ex13.py', 'apple', 'orange', 'yellow']
# The script is called:  Ex13.py
# Your first variable is:  apple
# Your second variable is:  orange
# Your Third variable is:  yellow
