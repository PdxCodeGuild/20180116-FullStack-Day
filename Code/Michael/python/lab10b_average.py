


nums = []
cont = True

while cont == True:
    number_entered = float(input("enter a number \n> "))
    nums.append(number_entered)

    done = input("are you finished?\n> ")
    if done == "yes":
        cont = False
    else:
        cont = True

number_sum = int(sum(nums))
list_length = int(len(nums))
print(f'the average is {number_sum / list_length}')







