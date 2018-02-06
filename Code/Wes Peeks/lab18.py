data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peeksu(data):
    peeks = []
    for i in range(1, len(data)-1 ):
        left = data[i-1]
        center = data[i]
        right = data[i+1]
        if left < center and right < center:
            peeks.append(i)
    return peeks

def valley(data):
    low_lands = []
    for i in range(1, len(data)-1):
        left = data[i-1]
        center = data[i]
        right = data[i+1]
        if left > center and right > center:
            low_lands.append(i)
    return low_lands

def pandv():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    print(peeks(data))
    print(low_lands(data))

pandv()