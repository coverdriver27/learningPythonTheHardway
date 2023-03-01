# Study Drills

countries = ["USA", "Canada", "France", "Japan", "Australia"]
car_brands = ["Toyota", "Ford", "BMW", "Tesla", "Honda"]
colors = ["red", "blue", "green", "yellow", "purple"]
fruits = ["apple", "banana", "orange", "kiwi", "mango"]
languages = ["Python", "Java", "C++", "JavaScript", "PHP"]
animals = ["lion", "tiger", "elephant", "giraffe", "rhinoceros"]
operating_systems = ["Windows", "macOS", "Linux", "iOS", "Android"]
instruments = ["guitar", "piano", "violin", "trumpet", "drums"]
vegetables = ["carrot", "broccoli", "tomato", "spinach", "cucumber"]
sports = ["football", "basketball", "tennis", "baseball", "hockey"]

print("\n We are just going to print one list(fruits) \n")
# Print the entire list
print(f"The list of fruits is:", fruits)

# Print the length of the list
print("The length of the list is:", len(fruits))

# Access the first element of the list
print("The first fruit is:", fruits[0])

# Access the last element of the list
print("The last fruit is:", fruits[-1])

# Append a new fruit to the end of the list
fruits.append("pineapple")
print("After appending a new fruit, the list is:", fruits)

# Insert a new fruit at a specific index
fruits.insert(2, "grape")
print("After inserting a new fruit, the list is:", fruits)

# Remove a fruit from the list
fruits.remove("banana")
print("After removing a fruit, the list is:", fruits)

# Sort the list in alphabetical order
fruits.sort()
print("After sorting the list, the list is:", fruits)

# Reverse the order of the list
fruits.reverse()
print("After reversing the list, the list is:", fruits)
