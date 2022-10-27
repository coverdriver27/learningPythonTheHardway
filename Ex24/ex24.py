# Exercise 24 - More Practise

# Bunch of print statements with using exceptions '\' , new lines '\n' , and tabbing '\t'
print("")
print("Let's practise everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

# creating a variable called poem, and assigning multiple lines of strings to the variable with """xyz"""
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition 
and requires an explanation 
\n\t\twhere there is none. 
"""

print("\n")
print("-------------------------------------------------------------------------------------------------------------")
print(poem)
print("-------------------------------------------------------------------------------------------------------------")

# assigning a int value to a variable
five = 10 - 2 + 3 - 6
# print(five)
print(f"This should be five: {five}")

# create a function
# the function passes one parameter variable
# within the function it does some actions
# and it returns some values
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# assign a int value to a variable
start_point = 10000
# assigning three variables to the function we created and within the parameter variable we are passing the variable
# from line 40
beans, jars, crates = secret_formula(start_point)
# line 43's variables gets mapped to the return values from line 37 of the function
# for example if we say apples, jars, crates = secret_formula(start_point), and change line 50's {beans} to {apples}
# this will still be mapped to the functions return values and return us the beans value we need

# remember that this is another way to format a string
# It's just like a f-string
print("With a starting point of: {}".format(start_point))
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10  # Gives a new value for the start_point variable

print("We can also do that this way:")
# create a new variable and call the function and pass the variable from line 53
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))  # since the function returns three values it
# will be mapped to each {} respectively

