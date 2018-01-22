# jackalope simulator
# two jackalopes # start at age 0
# make them age
# Age 4-8, start reproducing
# after 10, kill them off (die of natural cuases)
# finish condition: (number of iterations unknown.) len(<1000),
# use while loop... while len(<10000)
# starting value, add one each iteration of loop
# keep track of year

# first two jackalopes
jackalopes = [5, 5]
year = 0

while len(jackalopes) < 1000:
    pair_count =  0
    year += 1
    for i in range(len(jackalopes)- 1, -1, -1):  #age increasing
        jackalopes[i] += 1
        if jackalopes[i] == 10:  # kill them off
            jackalopes.pop(i)  # method on list
        if 4 <= jackalopes[i] <= 8: #if they are breeding age
            pair_count += 1  # breed jackalopes. number of jackalpes of b reeding age / 2
    pair_count //= 2
    for i in range(pair_count):
        jackalopes.append(0)

print('Year: ', year)
print(jackalopes)
