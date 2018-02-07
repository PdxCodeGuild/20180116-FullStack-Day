"""THE IM-POSSIBLE GAME"""

import random
import timeit

while True:

    nanosecond = .1


    def test():
        split_time = []
        for i in range(int(nanosecond)):
            split_time.append(i)


    if __name__ == '__main__':
        print(timeit.timeit("test()", setup="from __main__ import test"))

        i = 1
    x = timeit.timeit("test()", setup="from __main__ import test")
    high = ['too high', 'too high ;)', 'still too high', 'number is too high', 'too high, good luck',
            'too high but the sky is the limit', 'JUST RAGE QUIT ALREADY']
    low = ['too low', 'still too low', 'low low', 'down low', 'low', 'meet me at the station way down low', 'JUST RAGE '
                                                                                                            'QUIT ALREADY']
    number_guess = float(input('Guess the number: '))

    if number_guess > x:  # telling user if too high
        print(random.choice(high))
    elif number_guess < x:
        print(random.choice(low))  # telling user if too low
    elif number_guess == x:
        print('You won and impossible game! The word "Impossible" says IM POSSIBLE. However, you still lost the GAME')
        break
    i += 1

    test()
