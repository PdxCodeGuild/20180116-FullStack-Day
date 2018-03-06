
city_times_dict = {
    'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
    'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
    'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
    'Portland': {'Boston': 3, 'Albany': 7},
    'Philadelphia': {'New York': 9}
}

# key is destination, value is (time, trip list)
best_times = {
    'Boston': {'Boston': [0, []], 'New York': [0, []], 'Philadelphia': [0, []], 'Albany': [0, []], 'Portland': [0, []]},
    'New York': {'Boston': [0, []], 'New York': [0, []], 'Philadelphia': [0, []], 'Albany': [0, []], 'Portland': [0, []]},
    'Philadelphia': {'Boston': [0, []], 'New York': [0, []], 'Philadelphia': [0, []], 'Albany': [0, []], 'Portland': [0, []]},
    'Albany': {'Boston': [0, []], 'New York': [0, []], 'Philadelphia': [0, []], 'Albany': [0, []], 'Portland': [0, []]},
    'Portland': {'Boston': [0, []], 'New York': [0, []], 'Philadelphia': [0, []], 'Albany': [0, []], 'Portland': [0, []]}
}



start = input('Please enter your starting city')
hops = int(input('How many hops'))



trip_dict = {0 : [[start]]}

for i in range(hops):
    new_list_of_trips = []
    current_list_of_trips = trip_dict[i]
    for trip in current_list_of_trips:
        last_city = trip[-1]
        next_cities = city_times_dict[last_city].keys()
        for city in next_cities:
            if city in trip:
               continue
            new_trip = []
            for item in trip:
                new_trip.append(item)
            new_trip.append(city)
            new_list_of_trips.append(new_trip)


    trip_dict[i+1] = new_list_of_trips


for j in range(hops):
    for trip in trip_dict[j]:
        hours_list = []
        print(trip)
        for i in range(len(trip)-1):
            hours_list.append(city_times_dict[trip[i]][trip[i+1]])
        print(hours_list)
        total_hours = sum(hours_list)
        print(total_hours)
        if best_times[start][trip[-1]][0] == 0 or total_hours <= best_times[start][trip[-1]][0]:
            best_times[start][trip[-1]][0] = total_hours
            best_times[start][trip[-1]][1] = trip




for key in best_times:
     print(f'The best time from {start} to {key} is {best_times[start][key][0]} hours via {best_times[start][key][1]}')

