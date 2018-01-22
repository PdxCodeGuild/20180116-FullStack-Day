inputN = input('please enter a list of number with comma')
inputN = inputN.split(",")
inputN = [int(i) for i in inputN]
peaks = list()
valleys = list()
peaks_and_valleys = list()


for i in range(1, inputN.__len__()-1):
    if inputN[i] < inputN[i - 1] and inputN[i] < inputN[i + 1]:
        valleys.append(i)
        peaks_and_valleys.append(i)
    elif inputN[i] > inputN[i - 1] and inputN[i] > inputN[i + 1]:
         peaks.append(i)
         peaks_and_valleys.append(i)


print(valleys)
print(peaks)
print(peaks_and_valleys)



