"""
Optional lab
LCR Simulator
"""

import random

player_list = []

print("Welcome to LCR! How many players are playing today?")
players = input("> ")
players = int(players)

for i in range(0, players):
    name = input("Enter a player name: ")
    player_list.append(name)

bank = {'Center': 0}

for i in range(0, players):
    bank[player_list[i]] = 3

print(f"\nThese are the starting values: {bank}")


def roll():
    roll = random.randint(1,7)
    if roll == 1:
        print("You rolled an 'L'. Pass a chip left!")
        result = "L"
    elif roll == 2:
        print("You rolled an 'R'. Pass a chip right!")
        result = "R"
    elif roll == 3:
        print("You rolled a 'C'. Put a chip in the middle!")
        result = "C"
    else:
        print("You rolled a '*'. Pass!")
        result = "*"
    return result


while True:                                             # while more than one player has chips, otherwise game ends
    players_left = players                              # initialize how many players left

    for i in range(0, players):
        if bank[player_list[i]] == 0:                              # if player has no chips, takes no turn
            print(f"\nNo chips. {player_list[i]} skips a turn")
            players_left -= 1
        else:
            if bank[player_list[i]] == 1:
                print(f"\nIt's {player_list[i]}'s turn to roll.")
                result = roll()
                if result == 'L':
                    bank[player_list[i]] -= 1
                    bank[player_list[i - 1]] += 1
                elif result == 'R':
                    if player_list[i] != player_list[players - 1]:
                        bank[player_list[i]] -= 1
                        bank[player_list[i + 1]] += 1
                    else:
                        bank[player_list[i]] -= 1
                        bank[player_list[0]] += 1
                elif result == 'C':
                    bank[player_list[i]] -= 1
                    bank['Center'] += 1
                else:
                    pass
            elif bank[player_list[i]] == 2:
                print(f"\nIt's {player_list[i]}'s turn to roll.")
                result = roll()
                if result == 'L':
                    bank[player_list[i]] -= 1
                    bank[player_list[i - 1]] += 1
                elif result == 'R':
                    if player_list[i] != player_list[players - 1]:
                        bank[player_list[i]] -= 1
                        bank[player_list[i + 1]] += 1
                    else:
                        bank[player_list[i]] -= 1
                        bank[player_list[0]] += 1
                elif result == 'C':
                    bank[player_list[i]] -= 1
                    bank['Center'] += 1
                else:
                    pass
                result = roll()
                if result == 'L':
                    bank[player_list[i]] -= 1
                    bank[player_list[i - 1]] += 1
                elif result == 'R':
                    if player_list[i] != player_list[players - 1]:
                        bank[player_list[i]] -= 1
                        bank[player_list[i + 1]] += 1
                    else:
                        bank[player_list[i]] -= 1
                        bank[player_list[0]] += 1
                elif result == 'C':
                    bank[player_list[i]] -= 1
                    bank['Center'] += 1
                else:
                    pass
            else:
                print(f"\nIt's {player_list[i]}'s turn to roll.")
                result = roll()
                if result == 'L':
                    bank[player_list[i]] -= 1
                    bank[player_list[i - 1]] += 1
                elif result == 'R':
                    if player_list[i] != player_list[players - 1]:
                        bank[player_list[i]] -= 1
                        bank[player_list[i + 1]] += 1
                    else:
                        bank[player_list[i]] -= 1
                        bank[player_list[0]] += 1
                elif result == 'C':
                    bank[player_list[i]] -= 1
                    bank['Center'] += 1
                else:
                    pass
                result = roll()
                if result == 'L':
                    bank[player_list[i]] -= 1
                    bank[player_list[i - 1]] += 1
                elif result == 'R':
                    if player_list[i] != player_list[players - 1]:
                        bank[player_list[i]] -= 1
                        bank[player_list[i + 1]] += 1
                    else:
                        bank[player_list[i]] -= 1
                        bank[player_list[0]] += 1
                elif result == 'C':
                    bank[player_list[i]] -= 1
                    bank['Center'] += 1
                else:
                    pass
                result = roll()
                if result == 'L':
                    bank[player_list[i]] -= 1
                    bank[player_list[i - 1]] += 1
                elif result == 'R':
                    if player_list[i] != player_list[players - 1]:
                        bank[player_list[i]] -= 1
                        bank[player_list[i + 1]] += 1
                    else:
                        bank[player_list[i]] -= 1
                        bank[player_list[0]] += 1
                elif result == 'C':
                    bank[player_list[i]] -= 1
                    bank['Center'] += 1
                else:
                    pass
        print(f"\nThese are the current values: {bank}")

    if players_left < 2:
        print(f"Game over! {list(bank.keys())[list(bank.values()).index(1)]} is the winner!")
        break

print(f"\nThe final results are: {bank}")