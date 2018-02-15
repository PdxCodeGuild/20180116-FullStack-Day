# VERSION 2: WITH X'S
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def draw_x(data):
	for i in range(0, len(data)):
		current = data[i]
		print('x ' * current)


draw_x(data)
