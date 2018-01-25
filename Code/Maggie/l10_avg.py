'''Averaging a list of numbers'''
from time import sleep
nums = [5, 0, 8, 3, 4, 1, 6]

def main():
    print('Averaging lists of numbers\n')
    print("\nWe are going to calculate the average from a given list of numbers")
    sleep(1)
    print('List One: ', nums)
    sleep(1)
    print('calculating average')
    sleep(1)
    cursum = 0
    for num in nums:
        print('current number', num, end=' ')
        print('sum =', cursum + num)
        cursum += num
        sleep(0.5)
    print('total = ', cursum)
    sleep(.5)
    print('number of items = ', len(nums))
    sleep(0.5)
    print('Average = Total divided by number of items = ', cursum/len(nums))
    sleep(1)



main()