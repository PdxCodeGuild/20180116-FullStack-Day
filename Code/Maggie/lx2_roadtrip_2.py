city_to_accessible_cities = {
  'Boston': {'New York', 'Albany', 'Portland'},
  'New York': {'Boston', 'Albany', 'Philadelphia'},
  'Albany': {'Boston', 'New York', 'Portland'},
  'Portland': {'Boston', 'Albany'},
  'Philadelphia': {'New York'}
}

from random import choice

# given list of connected cities

def hop_twice(city):
    hop_dest = city_to_accessible_cities[city]
    two_hop = []
    for key in hop_dest:
        for value in city_to_accessible_cities[key]:
            if value not in two_hop:
                two_hop.append(value)
    return two_hop

def run():
    starting_city = choice(list(city_to_accessible_cities.keys()))
    print('Let\'s go on a roadtrip!')
    current_city = starting_city
    while True:
        print(f'You\'re currently in {current_city}. Where would you like to go?')
        print(f'Two hops away: {hop_twice(current_city)}')
        print(f'One hop away: {city_to_accessible_cities[current_city]}')
        dest = input('Your choice (or enter q to quit): ')
        if dest in city_to_accessible_cities[current_city]:
            print(f'Ok. Hopping over to {dest}.\n')
            current_city = dest
        elif dest not in city_to_accessible_cities[current_city]:
            print('Invalid choice. Try again')
            continue
        elif dest.lower() == 'q':
            print('Ok! Thanks for hopping with us. See you again soon!')
            break
        else:
            print('Invalid choice. Try again.\n')
            continue

run()