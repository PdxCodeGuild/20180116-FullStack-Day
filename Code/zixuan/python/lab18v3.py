height = input('please enter a list of number with comma')
height = height.split(",")
height = [int(i) for i in height]

water = ['0' for n in range(len(height))]

print(height)
print(water)

left = 0
left_max = 0
right = len(height) - 1
right_max = 0

while left <= right:
    if left_max <= right_max:
        if height[left] < left_max:
            # add water
            water[left] = left_max - height[left]
        else:
            left_max = height[left]
        left = left + 1
    else:
        if height[right] < right_max:
            # add water
            water[right] = right_max - height[right]
        else:
            right_max = height[right]
        right = right - 1


for i in range(len(height)):
    s = 'X '*int(height[i]) + 'O '*int(water[i])
    print(s)
