# Using string formatting codes
age = 25
height = 1.75
name = "John"

print("My name is %s and I'm %d years old." % (name, age))
print("My height is %f meters." % height)
print("My height is %.2f meters." % height)
print("The value of pi is approximately %f." % 3.141592653589793)
print("The value of pi is approximately %.2f." % 3.141592653589793)
print("The decimal value of 15 is %d." % 15)
print("The octal value of 15 is %o." % 15)
print("The hexadecimal value of 15 is %x." % 15)
print("The character corresponding to ASCII value 65 is %c." % 65)
print("The percentage sign can be printed using %%.")

# Using f-strings
print(f"My name is {name} and I'm {age} years old.")
print(f"My height is {height:.2f} meters.")

"""
This program uses various string formatting codes to format and print out strings. It includes examples of using %d for
integers, %f for floats, %s for strings, %o for octal values, %x for hexadecimal values, %c for ASCII characters, and %% 
to print a percentage sign. It also includes examples of using f-strings for string interpolation.
"""