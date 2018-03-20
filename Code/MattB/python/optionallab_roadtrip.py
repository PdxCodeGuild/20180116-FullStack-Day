city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

start_city = input('Enter a city: ')

print('Cities accessible from one hop: ' + ','.join(city_to_accessible_cities[start_city]))


def set_to_list(city):
    cities = city_to_accessible_cities[city]
    count = 0
    city_string = ''
    if len(cities) > 1:
        while count <= len(cities) + 1:
            city_string += cities.pop() + ', '
            count += 1
        city_list = city_string.split(', ')
        city_list.remove('')
        return city_list
    elif len(cities) == 1:
        city_list = []
        lone_city = cities.pop()
        city_list.append(lone_city)
        return city_list


one_hop_list = set_to_list(start_city)
out_set = set([])


for i in range(0, len(one_hop_list)):
    out_set.update(city_to_accessible_cities[one_hop_list[i]])

print('Cities accessible from two hops: ' + ', '.join(out_set))







