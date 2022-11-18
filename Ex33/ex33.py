"""
Exercise 33 : While Loops

Intro tp while-loops
Remember unlike for loops, while loops are un-bounded (loop for every if conditions are not properly defined)
When writing while loops, for best practise write the while loops and right after define
the increment condition (for example variable = variable + 1) so it does not loop forever, and then append
good way to remember, a while loop, its a if statement and then a jump up to the condition

"""

i = 0
numbers = []

# while loops are unbounded
while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)  # .append function adds element to the list and keeps adding elements to the end of the list

    # i = i + 1 --> if i never changes this loop will run forever
    i = i + 1
    print("Number now: ", numbers)
    print(f"At the bottom i is {i}")
    # print(">>>>> After one loop")
    # End of the while loop, in the while loop it keeps checking for the while condition is true each time the code
    # block his the end of the loop

# print(">>>>>>>> after while loop")
print("The numbers: ")

for num in numbers:
    print(num)
    # print(numbers)

print("\n>>>>>>> Before function <<<<<<<<<<<\n")

def while_loop (range, increment):
    rng = 0
    numbers2 = []

    while rng < range:
        print(f"At the top rng is {rng}")
        numbers2.append(rng)

        rng = rng + increment
        print(f"Numbers now: ", numbers2)
        print(f"At the bottom rng is {rng}")

    print("The Numbers: ")

    for num2 in numbers2:
        print(num2)

while_loop(10, 2)

"""
converting the above while loop to a for-loop
"""

print("\n>>>>>> Now lets continue to run the same while-loop as a for loop <<<<<<<<<<<<<<\n ")

numbers3 = []

for b in range(0, 6):
    print(f"At the top b is {b}")
    numbers3.append(b)
    print(f"Numbers now: ", numbers3)
    print(f"At the bottom b is {b + 1}")

print("The Numbers: ")
for c in numbers3:
    print(c)
    # print("The Numbers:", c)
    # print(c)



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
#
# >>>>>>> Before function <<<<<<<<<<<
#
# At the top rng is 0
# Numbers now:  [0]
# At the bottom rng is 1
# At the top rng is 1
# Numbers now:  [0, 1]
# At the bottom rng is 2
# At the top rng is 2
# Numbers now:  [0, 1, 2]
# At the bottom rng is 3
# At the top rng is 3
# Numbers now:  [0, 1, 2, 3]
# At the bottom rng is 4
# At the top rng is 4
# Numbers now:  [0, 1, 2, 3, 4]
# At the bottom rng is 5
# At the top rng is 5
# Numbers now:  [0, 1, 2, 3, 4, 5]
# At the bottom rng is 6
# At the top rng is 6
# Numbers now:  [0, 1, 2, 3, 4, 5, 6]
# At the bottom rng is 7
# At the top rng is 7
# Numbers now:  [0, 1, 2, 3, 4, 5, 6, 7]
# At the bottom rng is 8
# At the top rng is 8
# Numbers now:  [0, 1, 2, 3, 4, 5, 6, 7, 8]
# At the bottom rng is 9
# At the top rng is 9
# Numbers now:  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# At the bottom rng is 10
# The Numbers:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
#


# Output with increments
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
#
# >>>>>>> Before function <<<<<<<<<<<
#
# At the top rng is 0
# Numbers now:  [0]
# At the bottom rng is 2
# At the top rng is 2
# Numbers now:  [0, 2]
# At the bottom rng is 4
# At the top rng is 4
# Numbers now:  [0, 2, 4]
# At the bottom rng is 6
# At the top rng is 6
# Numbers now:  [0, 2, 4, 6]
# At the bottom rng is 8
# At the top rng is 8
# Numbers now:  [0, 2, 4, 6, 8]
# At the bottom rng is 10
# The Numbers:
# 0
# 2
# 4
# 6
# 8

# Output with a while loop converted to a for loop
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
#
# >>>>>>> Before function <<<<<<<<<<<
#
# At the top rng is 0
# Numbers now:  [0]
# At the bottom rng is 2
# At the top rng is 2
# Numbers now:  [0, 2]
# At the bottom rng is 4
# At the top rng is 4
# Numbers now:  [0, 2, 4]
# At the bottom rng is 6
# At the top rng is 6
# Numbers now:  [0, 2, 4, 6]
# At the bottom rng is 8
# At the top rng is 8
# Numbers now:  [0, 2, 4, 6, 8]
# At the bottom rng is 10
# The Numbers:
# 0
# 2
# 4
# 6
# 8
#
# >>>>>> Now lets continue to run the same while-loop as a for loop <<<<<<<<<<<<<<
#
# At the top b is 0
# Numbers now:  [0]
# At the bottom b is 1
# At the top b is 1
# Numbers now:  [0, 1]
# At the bottom b is 2
# At the top b is 2
# Numbers now:  [0, 1, 2]
# At the bottom b is 3
# At the top b is 3
# Numbers now:  [0, 1, 2, 3]
# At the bottom b is 4
# At the top b is 4
# Numbers now:  [0, 1, 2, 3, 4]
# At the bottom b is 5
# At the top b is 5
# Numbers now:  [0, 1, 2, 3, 4, 5]
# At the bottom b is 6
# The Numbers:
# 0
# 1
# 2
# 3
# 4
# 5