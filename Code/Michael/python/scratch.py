states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'WI': 'Detroit',
    'FL': 'Jacksonville'
}

# print(cities)
cities['NY'] = 'New York'
cities['OR'] = 'Portland'
# print(cities)

# print('-' * 60)
# print("NY State has: ", cities['NY'])
# print("OR State has: ", cities['OR'])
#
# print('-' * 60)
# print("Michigan's abbreviation is: ", states['Michigan'])
# print("Florida's abbreviation is: ", states['Florida'])

print('-' * 60)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])
