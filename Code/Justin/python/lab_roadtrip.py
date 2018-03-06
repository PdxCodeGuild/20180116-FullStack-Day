
city_to_accessible_cities = {
    'Boston': {'New York', 'Albany', 'Portland'},
    'New York': {'Boston', 'Albany', 'Philadelphia'},
    'Albany': {'Boston', 'New York', 'Portland'},
    'Portland': {'Boston', 'Albany'},
    'Philadelphia': {'New York'}
}


city_dict = {
    'Boston': {'New York', 'Moscow'},
    'New York': {'Boston', 'Albany', 'Philadelphia'},
    'Albany': {'Boston', 'New York', 'Portland'},
    'Portland': {'Boston', 'Albany', 'Aukland'},
    'Philadelphia': {'New York'},
    'Moscow': {'Beijing', 'Boston', 'Dallas'},
    'Aukland': {'Timbuktu', 'Atlantis'},
    'Atlantis': {},
    'Timbuktu': {'Beijing'},
    'Beijing': {'New York'}
}



start = input('Please enter your starting city')
hops = int(input('How many hops'))

#Initial destination set and trips dictionary (keys will be number hops and values will be destination set)

destinations = {0 : {start}}


print(f'From {start}')
for i in range(0,hops):
    destinations[i + 1] = set()
    for item in destinations[i]:
        destinations[i+1] = destinations[i+1].union(city_dict[item])
    print(f'In {i+1} hops you can go to  {destinations[i+1]}')

