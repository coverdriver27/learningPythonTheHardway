# Exercise 19: Functions and Variables


# We are writing out function that takes two parameter variables, and defining what the function does
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} Boxes of Crackers!!")
    print("Well That is enough for a Party! ")
    print("Get a blanket. \n")

print("We can just give the function numbers directly:")  # Printing a f-string
cheese_and_crackers(20, 30)  # Passing two values to the variables we set in the cheese_and_crackers function

print("OR, we can use the variables from our script:")  # regular ol print statement
amount_of_cheese = 10  # assigning a int value to a random variable
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)  # running our function and passing two random variables

print("We can even do math inside too:")  # print statement
cheese_and_crackers(10 + 20, 5 + 6)  # doing math operations to obtain a value to pass to our function as a parameter

print("We can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)  # we already set a value to the variable, just
# adding another int value to the pre-set variable from above

print("Can we pass a string a parameter value? ")
cheese_and_crackers("100", "200")  # We are able to
