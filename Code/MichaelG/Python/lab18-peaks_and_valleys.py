#                         p        v              p        v
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

for i in range(1, len(data)-1):
    if data[i-1] < data[i] > data[i+1]:
        dtp2 = data[i]
        dpt2 = str(dtp2)
        print('peak ' + dpt2)
    elif data[i-1] > data[i] < data[i+1]:
        dtp1 = data[i]
        dpt1 = str(dtp1)
        print('valley ' + dpt1)






