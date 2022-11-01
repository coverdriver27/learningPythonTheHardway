# Exercise 32 : Loops and Lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
# print(fruits, change, the_count)
# print(">>>>>", repr(fruits))

# this first kind of for loop goes through a list
for number in the_count:
    print(f"This is count {the_count}")

for fruit in fruits:
    print(f"A fruit of type: {fruits}")

# Also we can go through mixed lists too
# Notice we have to use () since we do not know what is in it

for i in change:
    print(f"I got {i}")

# We also can build lists, first start with a empty on
elements = []

# Then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

# Now we can print them out too
for i in elements:
    print(f"Element was: {i}")
