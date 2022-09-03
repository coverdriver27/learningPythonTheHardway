my_name = 'Dhulian Pereira'
my_age = 27 # we don't need qoutes when declaring numbers or integers
my_height = 82 # inches
my_weight = 165 # lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

# let's do print statements with f
# The f lets you do or run python within the print statement
# to do python within the print statement you should use {} braces
print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
# We can use f in the print command to do python withing the command
total = my_age + my_height + my_weight
print(f"If i add {my_age}, {my_height}, and {my_weight} I get {total}.")

print("--------------------------------------------------------------------------")
print("--------------------------------------------------------------------------")

# Study Drills
name = 'Dhulian Pereira'
age = 27 # we don't need qoutes when declaring numbers or integers
height = 82 # inche's
weight = 165 # lbs
eyes = 'Brown'
teeth = 'White'
hair = 'Black'
height_in_cm = height * 2.54 # inches to cm conversion
weight_in_kg = weight * 0.45 # lbs to Kg conversion

# let's do print statements with f
# The f lets you do or run python within the print statement
# to do python within the print statement you should use {} braces
print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He is {height_in_cm} cm tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's {weight_in_kg} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
# We can use f in the print command to do python withing the command
total = age + height + weight
print(f"If i add {age}, {height}, and {weight} I get {total}.")