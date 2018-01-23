import random



def build_data():
    # Build a a data list starting at a random integer 1-9 and then randomly adding 1 or -1 to get next value
    d = [random.randint(1, 9)]
    for i in range(24):
        if d[-1] == 9:
            d.append(8)
        elif d[-1] == 1:
            d.append(2)
        else:
            d.append(d[-1] + random.choice([1, -1]))
    return(d)



def find_peaks(d):
    # Variable d is local data list
    p = [0]
    for i in range(1, len(d) - 1):
        if d[i - 1] < d[i] and d[i + 1] < d[i]:
            p.append(1)
        else:
            p.append(0)
    p.append(0)
    return p

def find_valleys(d):
    # Variable d is local data list
    v = [0]
    for i in range(1, len(d) - 1):
        if d[i - 1] > d[i] and d[i + 1] > d[i]:
            v.append(1)
        else:
            v.append(0)
    v.append(0)
    return v

def get_peaks_and_valleys(p, v):
    p_v = []
    for i in range(len(p)):
        if p[i] == 1:
            p_v.append('^')
        elif v[i] == 1:
            p_v.append('V')
        else:
            p_v.append('-')
    return p_v

def make_line(val, d):
    # variable d is local data set
    # variable val is current height of
    line_list = []
    for i in range(len(d)):
        if d[i] >= val:
            line_list.append(' X ')
        else:
            line_list.append('   ')


    # Here we check for spaces in between X's
    # and replace them with O's
    for i in range(len(line_list) - 2):
        if (line_list[i] == ' X ' or line_list[i] == ' O ') and line_list [i+1] == '   ' and ' X ' in line_list[i+2:]:
            line_list[i + 1] = ' O '
    # Return a string
    return ''.join(line_list)



def draw_image(d): # variable d is local data set
    for i in range(9, 0, -1):
        print(make_line(i, d))


# Initialize data set
data = build_data()


peaks = find_peaks(data)
valleys = find_valleys(data)

peaks_and_valleys = get_peaks_and_valleys(peaks, valleys)

draw_image(data)

print(data, ' Data')
print(peaks, ' Peaks')
print(valleys, ' Valleys')
peak_indices = []
valley_indices = []
for i in range(len(peaks)):
    if peaks[i] == 1:
        peak_indices.append(i)
    if valleys[i] == 1:
        valley_indices.append(i)

print('', '  '.join(peaks_and_valleys), '  Peaks and Valleys')
print('')
print(peak_indices, 'Indices of peaks: ')
print(valley_indices, 'Indices of valleys: ')
