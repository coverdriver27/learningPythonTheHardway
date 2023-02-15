import random
"""
Exercise 36: Designing and Debugging

Now that you know if-statements, I'm going to give you some rules for for-loops and while-loops that will keep you out
of trouble. I'm also going to give you some tips on debugging so that you can figure out problems with your program.
Finally, you will design a little game similar to the last exercise but with a slight twist.
"""

"""
Create a simple game called "Guess the Number". In this game, the computer will choose a random number 
between 1 and 100, and the player will have to guess what the number is. The computer will give hints to the player 
about whether their guess is too high or too low, and the game will continue until the player guesses 
the correct number.
"""


# Generate a random number between 1 and 100
number = random.randint(1, 100)

# Set the player's initial number of guesses to 0
guesses = 0

# Print out the game instructions
print("Welcome to 'Guess the Number'! I'm thinking of a number between 1 and 100. Can you guess what it is?")

# Start the game loop
while True:
    # Ask the player to enter a guess
    guess = int(input("Enter your guess: "))

    # Increment the player's number of guesses
    guesses += 1

    # Check if the guess is correct
    if guess == number:
        print("Congratulations, you guessed the number in", guesses, "guesses!")
        break
    # Check if the guess is too high
    elif guess > number:
        print("Too high! Try again.")
    # Check if the guess is too low
    else:
        print("Too low! Try again.")
