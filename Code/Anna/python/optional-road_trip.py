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
