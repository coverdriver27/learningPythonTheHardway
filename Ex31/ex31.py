"""
# Exercise 31 : Making Decisions

# Using if-statements --> if not, leads to elif (Else-if) Statements --> If nothing then else-statements
# Changed the code a here to use print statements that has multiple lines in """ """ quotes
"""

print("""
You enter a dark room with two doors!
Do you go through door #1 or Door #2?
""")

door = input("1 or 2 > ")  # printing it this way so the user will visually see that they need to input 1 or 2

# from this point on, we will start to work on our if --> elif --> Statements
# Note: you can see of the if-statements are indented to be branched withing to perform certain actions
if door == "1":
    print("There is a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("""
    1. Take the cake.
    2. Scream at the bear?
    """)  # doing three quotes than having to do two print statements here

    bear = input("1 or 2 > ")

    if bear == "1":
        print("Bear eats your face off. Good Job!!!")
    elif bear == "2":
        print("The bear eats your legs off. Good Job!!!")
    else:
        print(f"Well, doing {bear} is probably better.")  # this is only printed out if the user does not input 1 or 2
        # but something different than the given choices
        print("Bear runs away, Congratulations!!!!!!")

elif door == "2":
    print("You stare into the endless abyss at cthulhu's retina.")
    print("""
    1. Blueberries.
    2. Yellow jacket clothespins.
    3. Understanding revolves yelling melodies. 
    """)

    insanity = input("1, 2 or 3 > ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good Job!!!")
    else:
        print(f"The insanity rots your eyes into a pool of much because you picked {insanity}")
        print("Good Job!!!!!")

else:
    print("You Still Stumble and fall and hit your head, Good Job!!!!")


twist = ("""
Now since we are at the end of the Game! 
Press "1" to cancel and exit the game. 
""")

press = input(twist)

if press == "1":
    print("""
    Just Kidding !!!!! 
    We are not done yet 
    You Still need to escape because the bear is on the loose!!!!!!
    Your options are as follows: 
        1. Run of foot to the nearest village. 
        2. Summon your inner goku 
        3. Take the abandoned jet outside the cave. 
    """)
    select = "Select a option 1, 2 or 3 > "
    pick = input(select)
    if pick == "1":
        print("Bears are fast, who we kidding your bear food!!!")
    elif pick == "2":
        print("Who we kidding you are just human so, you are bear food!")
    elif pick == "3":
        print("Who are we kidding you do not know how to handle a jet, so you crash!!!!, and still bear food")
    else:
        print(f"You avoided convention by picking {pick} so you survived!!! Congrats! ")

else:
    print("You Avoided convention so you, SURVIVED !!!!!")




