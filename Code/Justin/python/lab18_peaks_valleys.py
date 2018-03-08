import random



def build_data():
    # Build a a data list starting at a random integer 1-9 and then randomly adding 1 or -1 to get next value
    d = [random.randint(1, 9)]
    for i in range(50):
        if d[-1] == 9:
            d.append(8)
        elif d[-1] == 1:
            d.append(2)
        else:
            d.append(d[-1] + random.choice([1, -1]))
    return(d)



def find_peaks():
    p = [0]
    for i in range(1, len(data) - 1):
        if data[i - 1] < data[i] and data[i + 1] < data[i]:
            p.append(1)
        else:
            p.append(0)
    p.append(0)
    return p

def find_valleys():
    # Variable d is local data list
    v = [0]
    for i in range(1, len(data) - 1):
        if data[i - 1] > data[i] and data[i + 1] > data[i]:
            v.append(1)
        else:
            v.append(0)
    v.append(0)
    return v

def join_peaks_and_valleys():
    p_v = []
    for i in range(len(peaks)):
        if peaks[i] == 1:
            p_v.append('^')
        elif valleys[i] == 1:
            p_v.append('V')
        else:
            p_v.append('-')
    return p_v


def draw_image(d): # variable d is local data set
    for i in range(9, 0, -1):
        line_list = [] # This will be a list of ' X ', ' O ', or '   ' later joined as a single string and printed
        # First j loop draws X' for values
        for j in range(len(data)):
            if data[j] >= i:
                line_list.append(' X ')
            else:
                line_list.append('   ')

        # Next we check for spaces in between X's and replace them with O's
        for j in range(len(line_list) - 2):
            if (line_list[j] == ' X ' or line_list[j] == ' O ') and \
                    line_list[j + 1] == '   ' and ' X ' in line_list[j + 2:]:
                line_list[j + 1] = ' O '
        print(''.join(line_list))



# Initialize data set
data = build_data()

# ID locations of peaks and valleys
peaks = find_peaks()
valleys = find_valleys()

# Combine peaks list and valleys list into one list
peaks_and_valleys = join_peaks_and_valleys()

draw_image(data)

print(data, ' Data')
print(peaks, ' Peaks')
print(valleys, ' Valleys')

# Initialize list to store indices of peakes and valleys
peak_indices = []
valley_indices = []

# Find index of each peak and valley and append to appropriate list
for i in range(len(peaks)):
    if peaks[i] == 1:
        peak_indices.append(i)
    if valleys[i] == 1:
        valley_indices.append(i)

print('', '  '.join(peaks_and_valleys), '  Peaks and Valleys\n')
print(peak_indices, 'Indices of peaks: ')
print(valley_indices, 'Indices of valleys: ')
