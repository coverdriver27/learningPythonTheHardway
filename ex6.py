types_of_people = 10  # Assigning the value of 10 to the variable
x = f"There are {types_of_people} types of people."  # Assigning a f-string to x so you can call a python variable within the string
# "" Double qoutes are strong
binary = "binary"  # Assigning a string to a variable
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."  # Assigning a f-string to the y variable so it can call two other variable values within the string

# Debug sesh
# if we forgot the f-string for y variable the print statement would have {} brackets within the print
# to debug we can run print(">>>>>>>>>>>>> After we assign a value to y",y)

print(x)
# Debugging print(">>>>>>>>>>>> Before we print y", y)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False

joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))  # .format is a formatting used in python that apply a format to a already created string.
# The {} braces is set to a .format and within the {} it finds the set value
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

weather = "It has been so hot in LA !!  {}"
degrees = "100 Degrees has been"

print(weather.format(degrees))
# when printing we can print the variable it self and use the .format to add in the value we want in the {} of the initially set variable

weather1 = "No Way!!!! what is that in celsius?  {}"
degrees1 = 40

print(weather1.format(degrees1))
