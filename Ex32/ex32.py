# Exercise 32 : Loops and Lists

# Create lists and add values/items intp it
the_count = [1, 2, 3, 4, 5]  # List of numbers(int)
fruits = ['apples', 'oranges', 'pears', 'apricots']  # List of strings
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']  # List of numbers and lists
# print(fruits, change, the_count)
# print(">>>>>", repr(fruits))

# this first kind of for loop goes through a list
# For loops - for loops can go through a list and stop at the end, while loops are not guaranteed to end
# Way to read a for loop - for every element in something call it something else, and do: (Branch out to do things)
for number in the_count:
    # Within this code block there is a variable names number is assigned to each element/value of the_count
    # go into the list, for each element ---> do this
    print(f"This is count {number}")

# Same as above
for fruit in fruits:
    # variable named fruit is assigned each element/value of fruits in the loop
    print(f"A fruit of type: {fruit}")

# Also we can go through mixed lists too
# notice we have to use () since we do not know what is in it
for i in change:
    # Same thing as above
    print(f"I got {i}")

# We also can build lists, first start with a empty on
elements = []

# Then use the range function to do 0 to 5 counts
for i in range(0, 7):
    # range will basically will make a list from range(0, n) ---> [0, ....... , n-1]
    # range(start, stop, step)
    print(f"Adding {i} to the list.")
    # elements += 1
    # append is a function that lists understand
    elements.append(i)  # The append method appends an element to the end of the list. just like str.strip() for strings

# print(">>> After range: i=", i) --> Debug

# Now we can print them out too
for i in elements:
    print(f"Element was: {i}")

print(elements)  # this will show elements = [0, 1, 2, 3, 4, 5 ] because we used the range function above stating (0, 6)

# howdy = elements[:]  # This will copy all the contents of the elements list to the howdy variable via [:]
# print(howdy)
# print(change)
# print(change[0])
# print(change[1])
#
# Output ---->
#
# This is count 1
# This is count 2
# This is count 3
# This is count 4
# This is count 5
# A fruit of type: apples
# A fruit of type: oranges
# A fruit of type: pears
# A fruit of type: apricots
# I got 1
# I got pennies
# I got 2
# I got dimes
# I got 3
# I got quarters
# Adding 0 to the list.
# Adding 1 to the list.
# Adding 2 to the list.
# Adding 3 to the list.
# Adding 4 to the list.
# Adding 5 to the list.
# Adding 6 to the list.
# Element was: 0
# Element was: 1
# Element was: 2
# Element was: 3
# Element was: 4
# Element was: 5
# Element was: 6
# [0, 1, 2, 3, 4, 5, 6]
