# Peaks and Valleys

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]  # the data to sort


# if the value at the previous and post index is lower/higher, index marks a peak/valley
def peaks(lst):
    pk_i = []
    for i in range(1, len(lst)-1):
        if lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            pk_i.append(i)
    return pk_i


def valleys(lst):
    v_i = []
    for i in range(1, len(lst)-1):
        if lst[i] < lst[i - 1] and lst[i] < lst[i + 1]:
            v_i.append(i)
    return v_i


def peaks_and_valleys(lst):
    pv_i = []
    for i in range(1, len(lst)-1):
        if lst[i] < lst[i - 1] and lst[i] < lst[i + 1]:
            pv_i.append(i)
        elif lst[i] > lst[i - 1] and lst[i] > lst[i + 1]:
            pv_i.append(i)
    return pv_i


def drawlist(lst):
    graph = ''
    for line in range(max(lst)):  # start with line 1, iterate through each line
        for i in range(len(lst)):  # iterate through each space (x value) in the line
            if lst[i] >= (max(lst) - line):  # the first line should be the max, second line = max -1
                graph += ' x '
            else:
                graph += '   '
        if line != max(lst) - 1:
            graph += '\n'  # skip a line at the end of each row, except for last line
    print(graph)
    print(data)


def draw_filled(lst):  # uses a toggle to switch from space to fill
    graph = ''
    fill = False
    water = 0
    for line in range(max(lst)):  # start with line 1, iterate through each line
        for i in range(len(lst)):  # iterate through each space (x value) in the line
            if lst[i] >= (max(lst) - line):  # the first line should be the max, second line = max -1
                graph += ' x '
                fill = True
            else:
                if fill:
                    graph += ' 0 '
                    water += 1
                else:
                    graph += '   '
        if line != max(lst) - 1:
            graph += '\n'  # skip a line at the end of each row, except for last line
        fill = False
    print(graph)
    print(data)
    print('amount of water collected: ', water, 'units')


drawlist(data)
print('Peaks at index: ', peaks(data))
print('Valleys at index: ', valleys(data))
print('Combined peaks and valleys: ', peaks_and_valleys(data), '\n')
draw_filled(data)
