height = input('please enter a list of number with comma')
height = height.split(",")
height = [int(i) for i in height]

peaks = list()
valleys = list ()
for i in range(len(height)-1):
    if i != 0 and i != len(height)-1:

      if height[i] > height[i-1] and height[i] > height[i+1]:
        peaks.append(i)
      if height[i] < height[i - 1] and height[i] < height[i + 1]:
        valleys.append(i)

print(peaks)
print(valleys)