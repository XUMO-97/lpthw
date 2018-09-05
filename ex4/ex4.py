# Defines the number of cars is 100.
cars = 100
# Defines the number of seats in each car.
space_in_a_car = 4.0
# Defines the number of drivers.
drivers = 30
# Defines the number of passengers.
passengers = 90
# Defines the number of cars not driven.
cars_not_driven = cars - drivers
# Defines the number of cars that are driven. 
cars_driven = drivers
# Defines the number of people can carpool.
carpool_capacity = cars_driven * space_in_a_car
# Defines the number of passengers in each car.
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# study drills 0:Explain this error in your own words. Make sure you use line numbers and explain why.
# Because there's no variable named car_pool_capacity,the correct name is carpool_capacity.

# study drills 1:I used 4.0 for space_in_a_car, but is that necessary? What happens if it’s just 4?
# It's unnecessary,it make the variable named "carpool_capacity" become a floating-point number.
# If there's just 4,the result of "carpool_capacity" is just 120.

# study drills 2:Remember that 4.0 is a “floating point” number. Find out what that means.
# It's just a floating point number.

# study drills 3:Write comments above each of the variable assignments.

# study drills 4:Make sure you know what = is called (equals) and that it’s making names for things.
# Yes, of course.

# study drills 5:Remember that _ is an underscore character.
# OK,I remember it.

# study drills 6:Try running Python as a calculator like you did before and use variable names to do your calculations. Popular variable names are also i, x, and j.
# Finished.