# Exercise 21: Functions Can Return Something

# here we are going to use return
# Return is basically a way for a function to pass a value back to who ever called them
# writing some functions and make them do some things
def add(a, b):  # This function takes two parameters
    print(f"ADDING {a} + {b}")   # regular fstring print statement
    return a + b  # here we are doing a arithmetic operation for the two variables passed

def substract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLY {a} x {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDE {a} / {b}")
    return a / b

# return can do arithmetic operations on variables and return the result when called

print("Let's do some math with the functions!")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# for the above variables, once the parameter values are passed and runs through the functions, the variables have new
# values assigned to them, you can see them from the below print statement

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for extra credit, type it in anyway

print("Here is a puzzle.")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
print(f"That becomes: {what}, Can you do it by hand?")  # this is a better visual print
