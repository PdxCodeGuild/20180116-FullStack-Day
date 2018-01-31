"""
Optional lab
Road Trip
"""

city_to_accessible_cities = {
    'Boston': {'New York', 'Albany', 'Portland'},
    'New York': {'Boston', 'Albany', 'Philadelphia'},
    'Albany': {'Boston', 'New York', 'Portland'},
    'Portland': {'Boston', 'Albany'},
    'Philadelphia': {'New York'}
}

print("This is the list of cities: Boston, New York, Albany, Portland, Philadelphia")
print("Which city are you starting from?")
start_city = input("> ")
all_cities = set()


def one_hop(city):
    hop = city_to_accessible_cities[city]
    return hop


def two_hop(cities):
    for i in range(0, len(two_hop_cities)):
        second_city = " and ".join(one_hop(two_hop_cities[i]))
        print(f"From {cities[i]} you can get to {second_city} in another hop.")
        all_cities.update(one_hop(two_hop_cities[i]))
    set_cities = " and ".join(all_cities)
    print(f"\nSo, all of the cities you could get to in two hops are: {set_cities}!")


one_hop_cites = " and ".join(one_hop(start_city))
two_hop_cities = one_hop_cites.split(' and ')


print(f"From {start_city} you can get to {one_hop_cites} in one hop.")
two_hop(two_hop_cities)


# Version 2

city_to_accessible_cities_with_travel_time = {
  'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
  'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
  'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
  'Portland': {'Boston': 3, 'Albany': 7},
  'Philadelphia': {'New York': 9},
}

# do this recursively!!

print("\nThis is the list of cities: Boston, New York, Albany, Portland, Philadelphia")
print("Which city are you starting from?")
start_city = input("> ")
print("What is your maximum number of hops?")
max_hops = input("> ")
max_hops = int(max_hops)
next_cities = []


def city_hopper(start_city, max_hops):
    for key in city_to_accessible_cities_with_travel_time[start_city]:
        if key not in next_cities:
            next_cities.append(key)
    max_hops -= 1
    if max_hops != 0:
        for city in next_cities:
            city_hopper(city, max_hops)
        return next_cities


hopped_cities = city_hopper(start_city, max_hops)

print(f"From {start_city} you can get to {' and '.join(hopped_cities)} in {max_hops} hops.")
