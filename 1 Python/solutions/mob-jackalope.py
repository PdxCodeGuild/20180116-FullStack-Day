# Jackalope Simulator

# two jackalopes, start at age 0
# make them age
# Ages 4 through 8, start reproducing
# after 10, kill them off (die of nat causes :P)

# finish condition: (number of iterations unknown.) .. len(<1000),
    #  use a while loop... while len(<1000)
# starting value, add one each iteration of loop
# keep track of year


# First two jackalopes
jackalopes = [0, 0]
year = 0

while len(jackalopes) < 1000:
    pair_count = 0
    year += 1
    for i in range(len(jackalopes)-1, -1, -1):
        jackalopes[i] += 1 # age increasing
        if jackalopes[i] == 10:  # kill them off
            jackalopes.pop(i)
        if 4 <= jackalopes[i] <= 8:  # if they are of breeding age
            pair_count += 1 # breed them!
    pair_count //= 2
    for i in range(pair_count):
        jackalopes.append(0)


print('Year: ', year)
print(jackalopes)

