def list_sum (num_list):

    if len(num_list) == 1:

        return num_list[0]
    else:

        return num_list[0] + list_sum(num_list[1:])

print(list_sum([3,6,8,23,67,0,9,12,-87]))