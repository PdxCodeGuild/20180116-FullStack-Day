city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}}

# Traveling from one city to an adjacent one is called a hop. Let the user enter a city.
# Print out all the cities connected to that city. Then print out all cities that could be reached through two hops.

where_to_start = input("What city would you like to start from? (Boston, New York, Albany, Portland, or Philadelphia)\n:")

print("You can get to", city_to_accessible_cities[where_to_start], "in one hop.")







#[0][0]