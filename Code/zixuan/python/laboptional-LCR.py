import random

number_of_players = int(input("please enter the number of players:"))
number_of_chip = int(input("please enter the original chips (greater than 3)"))



class Player:

    def __init__(self, chips, right=None, left=None):
        self.chip = int(chips)
        self.right = right
        self.left = left

    def set_left(self, left_player):
        self.left = left_player

    def set_right(self, right_player):
        self.right = right_player

    def roll_dice(self):

        if self.chip > 3:
            roll_time = 3
        else:
            roll_time = self.chip
        for i in range(roll_time):
            out = random.randint(1, 6)
            if out == 1:
                print("give left")
                self.left.chip += 1
                self.chip -= 1
            elif out == 2:
                print("give right")
                self.right.chip += 1
                self.chip -= 1
            elif out == 3:
                print("give center")
                self.chip -= 1
            else:
                print("stay same")




def creat_player_list():
    player_list = []
    for i in range(number_of_players):
        if i > 0 and i < number_of_players - 1:
            player_list[i - 1].set_right(Player(number_of_chip, None, player_list[i - 1]))
            player_list.append(player_list[i - 1].right)

        elif i == 0:
            player_list.append(Player(number_of_chip))
        elif i == number_of_players - 1:
            player_list.append(Player(number_of_chip, player_list[0], player_list[i - 1]))
            player_list[i-1].set_right(player_list[i])
            player_list[0].set_left(player_list[i])

    return player_list


def win(player_list):
    n = 0
    winner = 0
    for i in range(len(player_list)):
        if player_list[i].chip != 0:
            n = n + 1
            winner = i
    if n == 1:
        print("winner is "+str(winner+1))
    return n == 1

def print1(player_list):
    for player in player_list:
        print(player.chip)
    print("XXXXXXXXX")


def main():
    player_list = creat_player_list()
    print1(player_list)

    while True:
        win_check = False
        for player in player_list:
            player.roll_dice()
            print1(player_list)
            win_check = win(player_list)
            if win_check:
                break
        if win_check:
            break


main()
