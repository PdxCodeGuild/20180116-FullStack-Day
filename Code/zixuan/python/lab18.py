inputN = input('please enter a list of number with comma')
inputN = inputN.split(",")
inputN = [int(i) for i in inputN]

maxN = max(inputN)
picture = [[0 for i in range(inputN.__len__())] for i in range(maxN)]

##################
peaks = list()

for i in range(0, inputN.__len__()):

    if i == 0 and inputN[i] > inputN[i + 1]:
        peaks.append(i)
    elif i == inputN.__len__() - 1 and inputN[i] > inputN[i - 1]:
        peaks.append(i)

    elif inputN[i] > inputN[i - 1] and inputN[i] > inputN[i + 1]:
        peaks.append(i)


###########
peak_index = 1

for i in range(0, inputN.__len__()):
    for j in range(0, maxN):
        picture[j][i] = ' '

for i in range(0, inputN.__len__(), +1):
    if i > peaks[peak_index] and peak_index < peaks.__len__()-1:
        peak_index = peak_index + 1

    for j in range(0, maxN):
        o = 0
        if peak_index - 1 >= 0:
            o = min(inputN[peaks[peak_index]], inputN[peaks[peak_index - 1]])

        if j < inputN[i]:
            picture[j][i] = 'X'
        elif j < o and i >= peaks[peak_index-1] and i <= peaks[peak_index]:
            print(peaks[peak_index])
            picture[j][i] = 'O'

for i in range(maxN - 1, -1, -1):
    for j in range(0, inputN.__len__()):
        print(picture[i][j]+' ', end='')
    print('')
