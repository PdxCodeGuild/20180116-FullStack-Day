"""
Define the following functions:
peaks - Returns the indices of peaks. A peak has a lower number on both the left and the right.
valleys - Returns the indices of 'valleys'. A valley is a number with a higher number on both the left and the right.
peaks_and_valleys - uses the above two functions to compile a single list of the peaks and valleys in order of
appearance in the original data.

"""
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9] #given data

length = len(data)

def peaks():
    i = 0
    peak = []
    while i < (length - 2):
        if data[i] < data[i+1] and data[i+1] > data[i+2]:
            peak.append(i+1)
        i += 1
    return peak

def valley():
    i = 0
    valley = []
    while i < (length - 2):
        if data[i] > data[i+1] and data[i+1] < data[i+2]:
            valley.append(i+1)
        i += 1
    return valley


def peaks_and_valleys():
    #create new list
    #append for len of lists
    #sorted() function


print(peaks())
print(valley())