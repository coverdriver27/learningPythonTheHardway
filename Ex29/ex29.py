# Exercise 29 : What If

# This exercise we are doing some if statements

people = 20
cats = 30
dogs = 15

# When we have a if-statement, if it is by itself the defined actions within the if statement are performed only if the
# statement is true

if people < cats:
    print("Too many cats! the world is doomed!")
# else:
#    print("Too many cats! the world is doomed!")

if people > cats:
    print("Not many cats! The world is saved")
# else:
#    print("Not many cats! The world is saved")

if people < dogs:
    print("The world is drooled on!")
# else:
#    print("The world is drooled on!")

if people > dogs:
    print("The world is now dry!")
# else:
#    print("The world is now dry!")

dogs += 5  # adds 5 to the current value of the dog variable (counter + 5)
# += is called the increment by operator
# dogs = dogs + 5  # another way
# print(">>>>>>>>>>>>Debug", dogs)

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are Dogs.")

# Initial output -->
#
# Too many cats! the world is doomed!
# The world is now dry!
# People are greater than or equal to dogs.
# People are less than or equal to dogs.
# People are Dogs.

# Output with some else statements
#
# Too many cats! the world is doomed!
# Not many cats! The world is saved
# The world is drooled on!
# The world is now dry!
# People are greater than or equal to dogs.
# People are less than or equal to dogs.
# People are Dogs.


