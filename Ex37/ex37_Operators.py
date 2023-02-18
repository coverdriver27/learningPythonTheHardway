# Using operators
a = 10
b = 3
c = [1, 2, 3, 4, 5]
d = {'name': 'John', 'age': 30}

# Arithmetic operators
print(a + b)
print(a - b)
print(a * b)
print(a ** b)
print(a / b)
print(a // b)
print(a % b)

# Comparison operators
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)
print(a == b)
print(a != b)

# Membership operators
print(3 in c)
print(6 not in c)
print('name' in d)
print('city' not in d)

# Identity operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y)
print(x is not y)
print(x is z)
print(x == y)

# Assignment operators
a += 5
b -= 1
c *= 2
e = 7
e //= 3
f = 11
f %= 3
g = 2
g **= 3
print(a, b, c, d, e, f, g)

"""
This program uses arithmetic operators like +, -, *, **, /, //, and % to perform math operations on variables. It also 
uses comparison operators like <, >, <=, >=, ==, and != to compare variables. The program also includes examples of 
using membership operators like in and not in to check if a value is in a list or dictionary, and identity operators 
like is and is not to compare object identities. Lastly, the program includes examples of using assignment operators 
like +=, -=, *=, /=, //=, %= and **= to update the values of variables.
"""