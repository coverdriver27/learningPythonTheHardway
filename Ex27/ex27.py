# Exercise 27 : Memorizing Logic

"""
and
or
not
!= (Not Equal)
== (Equal)
>= (Greater-than-equal)
<= (Less-than-equal)
True
False
"""

cat = "cat"
dog = "dog"

animal = cat and dog

print(animal) # this only prints dog

animal = dog and cat

print(animal)

test = True and False
print(test)
test = True and True
print(test)
test = True or False
print(test)

cat = 20
dog = 50
print(f"""
Cat = {cat}
Dog = {dog}
""")
print(f"Is cat equal to dog: {cat == dog}")
print(f"Is cat not equal to dog: {cat != dog}")
print(f"Is cat greater that a dog: {cat >= dog}")
print(f"Is cat less than or equal to dog: {cat <= dog}")

print(100 == 10)
print(100 == 100)
print(100 != 10)
print(100 != 100)

# Outputs
#
# dog
# cat
# False
# True
# True
#
# Cat = 20
# Dog = 50
#
# Is cat equal to dog: False
# Is cat not equal to dog: True
# Is cat greater that a dog: False
# Is cat less than or equal to dog: True
# False
# True
# True
# False
