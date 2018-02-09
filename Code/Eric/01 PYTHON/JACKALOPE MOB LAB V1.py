#JACKALOPE SIM

# two jackalopes; start at age 0
# make aging
# ages 4 through 8, start reproducing
# after 10 years, die

# finish condition: number of iterations unknown. len(<1000
	#   use while loop: while len() < 1000
	#starting value, add one each iteration of loop
	# keep track of year

jackalopes = [0, 0]
year = 0

while len(jackalopes) < 1000:
	pair_count = 0
	year += 1
	for i in range(len(jackalopes)-1, -1, -1): #aging
		jackalopes[i] += 1
		if jackalopes[i] == 10: #death
			jackalopes.pop(i)
		if 4 <= jackalopes[i] <= 8:  #if jackalopes are mating age
			pair_count += 1  #mate: number of jackalopes of mating age / 2
		#print(pair_count // 2) #mating pairs
	pair_count //= 2
	for i in range(pair_count):
		jackalopes.append(0)


print('year: ', year)
print(jackalopes)
