# Setting a bunch of variables to values
cars = 100
space_in_a_car = 4  # Remember that 4.0 is a floating point number
# Python does not know spacing for variables, so we use _ as a character to visually represent a space
drivers = 30
drivers2 = 31
passengers = 90
cars_not_driven = cars - drivers  # Using variables to perform math operations
cars_driven = drivers  # Setting a variable to previously defined value variable
carpool_capacity = cars_driven * space_in_a_car
carpool_capacity2 = drivers2 * space_in_a_car
average_passengers_per_car = passengers / cars_driven
weather_today = 1 > 0

# now that we set variable values, lets use these guys in print statements
# Note that when printing variables we do not need "" as the variable is already set
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("In California we can transport", carpool_capacity2, "people tomorrow.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
print("Is there rain forecasted for today?", weather_today)
