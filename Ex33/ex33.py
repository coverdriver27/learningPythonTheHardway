# Exercise 33 : While Loops

# Intro tp while-loops
# Remember unlike for loops, while loops are un-bounded (loop for every if conditions are not properly defined)
# When writing while loops, for best practise write the while loops and right after define
# the increment condition (for example variable = variable + 1) so it does not loop forever, and then append
# good way to remember, a while loop, its a if statement and then a jump up to the condition

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Number now: ", numbers)
    print(f"At the bottom i is {i}")
    # print(">>>>> After one loop")

# print(">>>>>>>> after while loop")
print("The numbers: ")

for num in numbers:
    print(num)
    # print(numbers)


# Output ---->
# At the top i is 0
# Number now:  [0]
# At the bottom i is 1
# At the top i is 1
# Number now:  [0, 1]
# At the bottom i is 2
# At the top i is 2
# Number now:  [0, 1, 2]
# At the bottom i is 3
# At the top i is 3
# Number now:  [0, 1, 2, 3]
# At the bottom i is 4
# At the top i is 4
# Number now:  [0, 1, 2, 3, 4]
# At the bottom i is 5
# At the top i is 5
# Number now:  [0, 1, 2, 3, 4, 5]
# At the bottom i is 6
# The numbers:
# 0
# 1
# 2
# 3
# 4
# 5