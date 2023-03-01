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