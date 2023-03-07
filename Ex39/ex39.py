"""
Exercise 39: Dictionaries, Oh Lovely Dictionaries
"""

# Create a mapping of state to abbreviation

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
# print(states)

# Create a basic set of states and some cities in them
# noinspection PyDictCreation
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
# print(states, cities)
# print(states + cities)

# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 50)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])
# print(f"also florida is call {states['Florida']}")

# Do it by using the state then cities dict
print("-" * 50)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])
# print(f"We can also call michigan's state be {cities[states['Michigan']]}")

# print every state abbreviation
print('-' * 50)
for state, abbrev in list(states.items()):
    print(f"{state} -> is abbreviated -> {abbrev}")

# print every city in state
print("-" * 50)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} -> Has the city -> {city}")

# now do both at the same time
print("-" * 50)
for state, abbrev in list (states.items()):
    print(f"{state} -> state is abbreviated -> {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 50)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, No Texas.")

# get a city with a default value
city = cities.get('TX', 'Does not Exist')
print(f"The city for the state 'TX' is: {city}")

print("-" * 50)
print(cities)


print("-" * 50)
print(states)