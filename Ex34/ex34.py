
# Exercise 34 - Accessing Elements of Lists

bugs = ["ant", "firefly", "beetle"]

print(bugs[0])

print("----------lets try for loops to access------------------------------")

for bug in bugs:
    print(bug)
print("----------lets try for accessing elements with given params------------------------------")
print(bugs[1:])  # this will print from index 1 and on
print(bugs[1:2])  # print values from 1 to 2 indexes
print(bugs[:2])  # prints values up to the 2nd index
print(bugs[:])  # Prints all values of the list
print(bugs[-1])  # Prints the last value of the list

print("-------------------Lets split a string and put it into a list now------------------------")

hello = "Hello World How Are You Today"
hello_array = hello.split(' ')  # This will split each word after a blank white space to add it into a list index
print(hello_array[:])
print(hello_array[2])
print(hello_array[-1])
print(hello_array[1:4])
