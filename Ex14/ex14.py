#  Exercise 14 - Prompting and Passing

from sys import argv  # From sys module we are getting the argv function like in Ex13

script, user_name, command = argv  # Passing how many arguments the script should have
prompt = f"{script} > "  # Just a variable set to a random string value

print(f"Hi! {user_name}, I'm the {script} Script.")  # f-Strings
print("I'd like to ask you some questions.")
print(f"Do you like me? {user_name}")
likes = input(prompt)  # Prompting the user with the prompt variable and saving the input as likes

print(f"Where do you live {user_name}?")
lives = input(prompt)  # Prompting the user with the prompt variable and saving the input as lives

print(f"What kind of computer do you have? {user_name} from {lives}")
computer = input(prompt)  # Prompting the user with the prompt variable and saving the input as computer

print("Do you play or know about the games Zork and Adventure?")
ans = input(prompt)


print(f"""
{command}
Alright, so said {likes} about liking me.
you live in {lives}. Not too sure where that is.
And you have a {computer} Computer!. Nice!!!.
Since you said {ans}, to the game you are awesome!, If not go play it.
""")  # here after prompting the user for input and saving them in variables we are passing it in the f-string

#  This script combines the use of argv function along with f-strings and """ """ prints

#  Initial Output from terminal -->

#  PS C:\Users\Ex14> python ex14.py john-doe
#  Hi! john-doe, I'm the ex14.py Script.
#  I'd like to ask you some question.
#  Do you like me? john-doe
#  > Yes
#  Where do you live john-doe?
#  > In the Cloud
#  What kind of computer do you have? john-doe from In the Cloud
#  > RoG Stix
#
#  Alright, so said Yes about liking me.
#  you live in In the Cloud. Not too sure where that is.
#  And you have a RoG Stix Computer!. Nice!!!.

#  After edits
#
#  PS C:\Ex14> python ex14.py john-doe start
#
# Hi! john-doe, I'm the ex14.py Script.
# I'd like to ask you some questions.
# Do you like me? john-doe
# ex14.py > Yes
# Where do you live john-doe?
# ex14.py > Cloud
# What kind of computer do you have? john-doe from Cloud
# ex14.py > Rog Stix
# Do you play or know about the games Zork and Adventure?
# ex14.py > Yes
#
# start
# Alright, so said Yes about liking me.
# you live in Cloud. Not too sure where that is.
# And you have a Rog Stix Computer!. Nice!!!.
# Since you said Yes, to the game you are awesome!, If not go play it.