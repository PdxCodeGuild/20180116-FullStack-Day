"""Ask the user to enter the numbers one at a time, putting them
into a list. If the user enters 'done', then calculate and display
the average. The following code demonstrates how to add an element
to the end of a list.
"""

nums = []
go_on = True

while go_on == True:
    a_number = float(input("Enter a number. \n:"))
    nums.append(a_number)
    print(f'You entered {a_number}')
    done = input("Are you finished?\n:")
    if done == "yes" or done == "y":
        go_on = False
    else:
        go_on = True

number_sum = int(sum(nums))
list_length = int(len(nums))
print(f'The average is {number_sum / list_length}')





