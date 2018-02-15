data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peak_finder(data):
	peaks = []
	peaks_i = []
	for i in range(1, len(data) - 1):
		previous = data[i - 1]
		current = data[i]
		next = data[i + 1]
		if previous < current > next:
			peaks_i.append(i)
			peaks.append(current)
	return peaks, peaks_i


def valley_finder(data):
	valleys = []
	valleys_i = []
	for i in range(1, len(data) - 1):
		previous = data[i - 1]
		current = data[i]
		next = data[i + 1]
		if previous > current < next:
			valleys_i.append(i)
			valleys.append(current)
	return valleys, valleys_i


def peaks_and_valleys(data):
	peaks = peak_finder(data)
	valleys = valley_finder(data)

	return peaks, valleys


p_v = peaks_and_valleys(data)


print(f'peaks: {p_v[0][0]} at indices: {p_v[0][1]}')
print(f'valleys: {p_v[1][0]} at indices: {p_v[1][1]}')
