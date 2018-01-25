import random

student_list = ['Justin', 'Jackson', 'Anna', 'Brianna', 'Maggie', 'Colton', 'Wes', 'Zixuan', "Ociel", "Sergio", "Eric", 'Michael M', 'Matt', 'Michael G', 'Scottie']

absent_student_list = ['Michael G', 'Matt', 'Scottie']



for i in range(len(absent_student_list)):
    student_list.remove(absent_student_list[i])


group_size = int(input("Size of group?"))
number_of_groups = len(student_list) // group_size

student_groups = []

while len(student_list) > 0:
    for i in range(number_of_groups):
        student = student_list.pop(random.randint(0, len(student_list)))
        student_groups[i].append(student)

print(student_groups)



index = 0
while len(student_list) > 0:
    student = student_list.pop(random.randint(0, len(student_list) - 1))
    student_groups[index].append(student)
    index = index + 1
    if index == number_of_groups:
        index = 0

print(student_groups)

-----
-----
import random
student_groups = []
random.shuffle(student_list)
for i in range(len(student_list):
    group = i % number_of_groups
    student_groups[group].append(student_list[i])

print(student_groups)




'''
students = []
group_size = int(input('How many players are playing RCL today?\n:'))
for group_num in range(player_number):
    student_group = []
    student_group = student_list.pop(random.randint(0. len(student_list)))
    players.append(student_group)
return students

'''