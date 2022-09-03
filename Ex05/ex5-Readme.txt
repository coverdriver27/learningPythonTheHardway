Exercise 5: More Variables and Printing

Now we'll do even more typing of variables and printing them out.
This time we'll use something called a "format string." Every time you put " (double-quotes) around a piece of text you
have been making a string. A string is how you make something that your program might give to a human.
You print strings, save strings to files, send strings to web servers, and many other things.

Strings are really handy, so in this exercise you will learn how to make strings that have variables embedded in them.
You embed variables inside a string by using a special {} sequence and then put the variable you want inside the {} characters.
You also must start the string with the letter f for "format", as in f"Hello {somevar}".
This little f before the " (double-quote) and the {} characters tell Python 3, "Hey, this string needs to be formatted.
Put these variables in there."

As usual, just type this in even if you do not understand it, and make it exactly the same.

Code to Write: -->

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")


What You Should See  -->

$ python3.6 ex5.py
Let's talk about Zed A. Shaw.
He's 74 inches tall.
He's 180 pounds heavy.
Actually that's not too heavy.
He's got Blue eyes and Brown hair.
His teeth are usually White depending on the coffee.
If I add 35, 74, and 180 I get 289.



Study Drills

-   Change all the variables so there is no my_ in front of each one. Make sure you change the name everywhere,
    not just where you used = to set them.

    >> Done

-   Try to write some variables that convert the inches and pounds to centimeters and kilograms.
    Do not just type in the measurements. Work out the math in Python.