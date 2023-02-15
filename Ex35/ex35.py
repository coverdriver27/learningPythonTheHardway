
"""
Exercise 35: Branches and Functions

You have learned if-statements, functions, and lists. Now it's time to bend your mind. Type this in, and see if you can
figure out what it's doing.
"""

from sys import exit

# create a bunch of functions and define what they do
def gold_room():
    print("This room is full of gold. How much do you want to take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man or Women, learn to type a number first!!!!")

    if how_much < 50:
        print("Nice, You're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!!!")

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    # While loop created for this function to do a certain thing, depending on the users input
    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()  # if the input matches "open door" this kicks off the gold_room function
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

# this function replaces the given string from functions above and passes it to its parameter and prints out
# also when the dead function is called the, the exit(0) terminates the game
def dead(why):
    print(why, "Good job!")
    exit(0)

# this function defines the start() of the game
def start():
    # Bunch of print statements after the game kicks off
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")  # prompt the user to input a choice and save the value to the choice variable
    # if-else statements on what to do depending on the user input
    if choice == "left":
        bear_room()  # if user inputs left, that kicks off the bear_room function that was defined above
    elif choice == "right":
        cthulhu_room()  # if user inputs right, that kicks off the cthulhu_room function that was defined above
    else:
        dead("You stumble around the room until you starve.")


start()  # this starts up the game, starting from the start() function defined on top

# Output
"""
You are in a dark room.
There is a door to your right and left.
Which one do you take?
> left
There is a bear here.
The bear has a bunch of honey.
The fat bear is in front of another door.
How are you going to move the bear?
> taunt bear
The bear has moved from the door.
You can go through it now.
> open door
This room is full of gold. How much do you want to take?
> 1000
You greedy bastard!!! Good job!

Process finished with exit code 0

"""

