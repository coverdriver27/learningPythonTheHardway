#resources: https://realpython.com/python-operators-expressions/#:~:text=In%20Python%2C%20operators%20are%20special,acts%20on%20are%20called%20operands.&text=A%20sequence%20of%20operands%20and,combining%20data%20objects%20into%20expressions.
print ("I will now count my chickens:")

print ("Hens", 25 + 30 / 6 )
print ("Roosters", 100 - 25 * 3 % 4) # % = Modulo, Remainder when a is divided by b

print ("Now i will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)


print ("Is it true that 3 + 2 < 5 -7?")

print (3 + 2 < 5 - 7) # returns a true or false

print ("What is 3 + 2 =", 3 + 2)
print ("What is 5 - 7 =", 5 - 7)

print ("Oh, that's why it's False.")

print ("How about some more.")

print ("Is it greater?", 5 > -2) # returns a true or false (Is 5 Greater than -2?)
print ("Is it greater or equal?", 5 >= -2) # returns a true or false
print ("Is it less or equal?", 5 <= -2) # return a true or false
print ("----------------------------------------------------------------")
print ("Now lets calculate you're annual salary:")
print ("$xy.xy * 2080")
print ("If i make 30$ a hour how much will i make annually? =", 30 * 2080)
print ("----------------------------------------------------------------")
print ("Testing floating point numbers")
#Testing Floating point numbers
float_val = (3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

formatted_float_value = "{:.2f}".format(float_val)
print(formatted_float_value)

float_val = (25 + 30 / 6)

formatted_float_value = "{:.2f}".format(float_val)
print(formatted_float_value)

float_val = (100 - 25 * 3 % 4)

formatted_float_value = "{:.2f}".format(float_val)
print(formatted_float_value)
