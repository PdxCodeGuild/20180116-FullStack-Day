cards = {1:"first",2:'second',3:'third'}
value_of_cards = 10
ace_value = 1
answer = []

# Get User Answer
for i in range(1,4):
    answer.append(input(f'What is your {cards[i]} card : '))


# calculate() gets the user input and gives it a nuerical value.
def caluculate(answer):
    total_value_of_card = 0
    ten_values = ['Q','J','K']
    single_value = ['2','3','4','5','6','7','8','9','10']

    for user_answer in answer:
        if user_answer in ten_values:
            total_value_of_card += 10
        if user_answer in single_value:
            total_value_of_card += int(user_answer)
    if 'A' in answer:
        if total_value_of_card <= 11:
            total_value_of_card += 10
        else:
            total_value_of_card += 1



    return total_value_of_card


# Call calculate and receive the value from the function.
final_value = caluculate(answer)

# Print results
if final_value < 17:
    print(f'{final_value} Hit! ')
elif 21 > final_value >= 17:
    print(f'{final_value} Stay! ')
elif final_value == 21:
    print(f'{final_value} Blackjack! ')
elif final_value > 21:
    print(f'{final_value} Busted! ')
