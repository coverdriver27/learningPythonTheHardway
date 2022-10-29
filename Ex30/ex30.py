# Exercise 30: Else and If

# here we are going to try out If-Else statements

# Adding values to variables
people = 30
cars = 40
trucks = 15

# Here we are giving our If-Statements more conditional statements to perform a particular action in the form of elif
# and else
# The logic behind this is if we have a If statement do this, if not do this, if nothing do this other thing,
# which goes from if --> elif --> else

if cars > people:
    # print(">>>>>>", cars, people)
    print("Are cars greater than people?:", cars > people)
    print("Then We should take the cars.")
elif cars < people:
    print("Are cars less than people?:", cars < people)
    print("The We Should not take the cars.")
else:
    print("Is Cars equal to people?:", cars == people)
    print("Then We cant decide.")

# We are doing the same thing as above here with comparing trucks and cars
if trucks > cars:
    print("Are trucks greater than cars?: ", trucks > cars)
    print("Then That is too many trucks.")
elif trucks < cars:
    print("Are trucks less than people?: ", trucks < cars)
    print("Then Maybe we should take the trucks.")
else:
    print("Are trucks equal to cars?: ", trucks == cars)
    print("Then We still can't decide.")

# here we are comparing people and trucks
# Only thing different here is that we only have two conditions here, if this then do this, if not for everything else
# do this,  if --> else
if people > trucks:
    print("Are people greater than trucks?:", people > trucks)
    print("Alright, lets just take the trucks.")
else:
    print("Are people not greater than trucks?:", people <= trucks)
    print("Let's just stay home")

# We are using alot of wen-diagram logic here
