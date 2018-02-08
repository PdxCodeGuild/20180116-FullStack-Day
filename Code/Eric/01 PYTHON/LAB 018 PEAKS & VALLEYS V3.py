#VERSION 3: WITH X'S AND O'S FOR WATER
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

#
# def peak_finder(data):
# 	peaks = []
# 	peaks_i = []
# 	for i in range(1, len(data) - 1):
# 		previous = data[i - 1]
# 		current = data[i]
# 		next = data[i + 1]
# 		if previous < current > next:
# 			peaks_i.append(i)
# 			peaks.append(current)
# 	return print('peaks: ' + str(peaks) + ' at indeces: ' + str(peaks_i))
#
#
# def valley_finder(data):
# 	valleys = []
# 	valleys_i = []
# 	for i in range(1, len(data) - 1):
# 		previous = data[i - 1]
# 		current = data[i]
# 		next = data[i + 1]
# 		if previous > current < next:
# 			valleys_i.append(i)
# 			valleys.append(current)
# 	return print('valleys: ' + str(valleys) + ' at indeces: ' + str(valleys_i))
#
#
# def peaks_and_valleys(data):
# 	peak_finder(data)
# 	valley_finder(data)
#
#
# peaks_and_valleys(data)


def draw_x(data):
	for i in range(0, len(data)):
		current = data[i]
		rain = 9 - current
		print('X ' * current + ('o ' * rain))


draw_x(data)
