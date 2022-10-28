# Exercise 30: Else and If

# here we are going to try out If-Else statements

people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We Should not take the cars.")
else:
    print("We cant decide.")

if trucks > cars:
    print("That is too many trucks.")
elif trucks < cars:
    print("Maybe we should take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, lets just take the trucks.")
else:
    print("Let's just stay home")
