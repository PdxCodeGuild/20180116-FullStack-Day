######finding peaks and valleys#######

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]


def peaks(data):
    for i in data[1:20]:
        if i > data([i]-1) and i > data([i]+1):
            pass
    #if the value in the data is greater than the last number and greater than the next, its a peak



def valleys(data):
    for i in data[1:20]:
        if i < data([i]-1) and i < data([i]+1):
            pass

def peaks_and_valleys():