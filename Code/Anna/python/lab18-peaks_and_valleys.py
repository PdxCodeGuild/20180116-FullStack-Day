"""
Lab 18
Peaks and valleys
"""

data_list = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peak_list = []
valley_list = []
both_list = []


def peaks(data):
    # get the peaks
    for i in range(0, len(data)):
        if data[i - 1] > data[i] < data[i + 1]:
            print(f"Valley: {data[i]}")
            peak_list.append(data[i])


def valleys(data):
    # get the valleys
    for i in range(0, len(data) - 1):
        if data[i - 1] < data[i] > data[i + 1]:
            print(f"Peak: {data[i]}")
            valley_list.append(data[i])


def peaks_and_valleys():
    # return both
    both_list = peak_list + valley_list
    return both_list


peaks(data_list)
valleys(data_list)

print(f"All the peaks: {peak_list}")
print(f"All the valleys: {valley_list}")
print(f"This list has both! {peaks_and_valleys()}")