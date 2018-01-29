#dight_list = input("please enter a list of numbers:")
dight_list = "4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5"
dight_list = dight_list.split(' ')
dight_list = [int(x) for x in dight_list]
dight_list.pop(len(dight_list)-1)
dight_list.reverse()
new_list=[]
for x in range(0, len(dight_list)):
    if x % 2 == 0:
        new_list.append(dight_list[x]*2)
    else:
        new_list.append(dight_list[x])
dight_list=[]
for x in range(0, len(new_list)):
    if new_list[x] > 9:
        dight_list.append(new_list[x]-9)
    else:
        dight_list.append(new_list[x])

sum = 0
for x in dight_list:
    sum += x

second = str(sum)[1]
print(second)