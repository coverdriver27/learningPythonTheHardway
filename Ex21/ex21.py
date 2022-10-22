# Exercise 21: Functions Can Return Something

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def substract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLY {a} x {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDE {a} / {b}")
    return a / b

print("Let's do some math with the functions!")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for extra credit, type it in anyway

print("Here is a puzzle.")

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
print(f"That becomes: {what}, Can you do it by hand?")
