# Things you can do with python dict's

# Define a dictionary:
print('-' * 10)
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(my_dict)

# Access a value by key:
print('-' * 10)
value = my_dict["key1"]
print(value)

# Add a new key-value pair:
print('-' * 10)
my_dict["key4"] = "value4"
print(my_dict["key4"])

# Modify the value of an existing key:
print('-' * 10)
my_dict["key2"] = "new_value2"
print(my_dict["key2"])
# Remove a key-value pair:
print('-' * 10)
del my_dict["key3"]
print(my_dict)
# print(my_dict["key3"])

# Check if a key exists in the dictionary:
print('-' * 10)
if "key1" in my_dict:
    print("Key exists!")

# Get the number of key-value pairs in the dictionary:
print('-' * 10)
num_items = len(my_dict)
print(num_items)

# Get a list of all keys in the dictionary:
print('-' * 10)
keys_list = list(my_dict.keys())
print(keys_list)

# Get a list of all values in the dictionary:
print('-' * 10)
values_list = list(my_dict.values())
print(values_list)

# Iterate over the keys or values in the dictionary:
print('-' * 10)
for key in my_dict:
    print(key, my_dict[key])

for value in my_dict.values():
    print(value)

# Merge two dictionaries:
print('-' * 10)
dict1 = {"key1": "value1", "key2": "value2"}
dict2 = {"key3": "value3", "key4": "value4"}
merged_dict = {**dict1, **dict2}
print(merged_dict)

# Clear all key-value pairs from the dictionary:
print('-' * 10)
my_dict.clear()
print(my_dict)

print('-' * 10)
print("More Stuff Below")
# Create a dictionary:
# You can create a dictionary by enclosing a comma-separated list of key-value pairs within curly braces {}.
my_dict = {"name": "John", "age": 30, "city": "New York"}

# Access values in a dictionary:
# You can access the value associated with a key in a dictionary using square bracket notation [] with the key.
# For example:
name = my_dict["name"]  # Returns "John"
age = my_dict["age"]  # Returns 30
city = my_dict["city"]  # Returns "New York"

# Modify values in a dictionary:
# You can modify the value associated with a key in a dictionary by assigning a new value using square bracket notation
# [] with the key. For example:
my_dict["age"] = 35  # Changes the value associated with the key "age" to 35

# Add new key-value pairs to a dictionary:
# You can add a new key-value pair to a dictionary by assigning a new value using square bracket notation [] with a new
# key. For example:
my_dict["email"] = "john@example.com"  # Adds a new key "email" with value "john@example.com"

# Delete key-value pairs from a dictionary:
# You can delete a key-value pair from a dictionary using the del keyword followed by square bracket notation [] with
# the key. For example:
del my_dict["age"]  # Deletes the key-value pair with key "age"

# Check if a key exists in a dictionary:
# You can check if a key exists in a dictionary using the in keyword. For example:
if "name" in my_dict:
    print("Name is present in the dictionary.")

# Get the keys or values of a dictionary:
# You can get a list of keys or values in a dictionary using the keys() and values() methods, respectively. For example:

keys_list = my_dict.keys()  # Returns a list of keys in the dictionary
values_list = my_dict.values()  # Returns a list of values in the dictionary

# Iterate over a dictionary:
# You can iterate over a dictionary using a for loop, which iterates over the keys by default. For example:

for key in my_dict:
    print(key, my_dict[key])


# This will print each key-value pair in the dictionary. You can also use the items() method to iterate over both keys
# and values together:
for key, value in my_dict.items():
    print(key, value)
