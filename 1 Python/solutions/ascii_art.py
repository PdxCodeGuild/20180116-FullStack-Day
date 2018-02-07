



import random

from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text' + Back.GREEN + 'and with a green background' + Style.RESET_ALL + Fore.BLUE + " hi")
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')




class DrawPattern1:
    def __init__(self, bounce=True, width=20, direction=True, column=0):
        self.bounce = bounce
        self.width = width
        self.direction = direction
        self.column = column

    def draw(self):
        time.sleep(0.05)
        print(Fore.GREEN + ' ' * self.column + '*')

        if self.direction:
            self.column += 1
        else:
            self.column -= 1

        if self.bounce:
            if self.column >= self.width:
                self.column = self.width - 2
                self.direction = not self.direction
            elif self.column < 0:
                self.column = 1
                self.direction = not self.direction
        else:
            if self.column >= self.width:
                self.column = 0
            elif self.column < 0:
                self.column = self.width - 1



class Ball:

    def __init__(self, position, color, velocity):
        self.position = position
        self.color = color
        self.velocity = velocity


class DrawPattern2:
    def __init__(self, n=4, width=80):
        self.balls = []
        self.width = width
        colors = [Fore.MAGENTA, Fore.BLUE, Fore.CYAN, Fore.GREEN]#, Fore.YELLOW, Fore.RED]
        for i in range(n):
            position = random.randint(0, self.width)
            while len(list(filter(lambda b: b.position == position, self.balls))) > 0:
                position = random.randint(0, self.width)
            color = random.choice(colors)
            self.balls.append(Ball(position, color, random.randint(-1, 1)))

    def draw(self):

        time.sleep(0.05)

        for b in self.balls:
            b.position += b.velocity

        for b1 in self.balls:
            for b2 in self.balls:
                if b1.position == b2.position:
                    b1.velocity *= -1
                    b2.velocity *= -1
            if b1.position > self.width:
                b1.position = self.width
                b1.velocity *= -1
            elif b1.position < 0:
                b1.position = 0
                b1.velocity *= -1


        for p in range(self.width):
            for b in self.balls:
                if b.position == p:
                    print(b.color + '*' + Fore.RESET, end='')
                    break
            else:
                print(' ', end='')
        print()

import time


dp = DrawPattern2(n=20)
for i in range(1000):
    dp.draw()





