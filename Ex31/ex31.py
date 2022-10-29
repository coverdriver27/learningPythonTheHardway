# Exercise 31 : Making Decisions

print("""
You enter a dark room with two doors!
Do you go through door #1 or Door #2?
""")

door = input("1 or 2 > ")

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


