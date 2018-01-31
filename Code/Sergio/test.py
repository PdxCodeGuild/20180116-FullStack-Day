import random

student_list = ['Justin', 'Jackson', 'Anna', 'Brianna', 'Maggie', 'Colton', 'Wes', 'Zixuan', 'OCL', 'Sergio', 'Eric', 'Michael M', 'Matt', 'Michael G', 'Scotttie']

absent_student_list = ['Michael G', 'Matt', 'Scottie']

print(len(student_list))


for i in range(len(absent_student_list)):
    student_list.remove(absent_student_list[i])

#

random.shuffle(student_list)

for i in range(len(student_list)):
    group = i % number_of_groups
    student_groups[group].append(student_list[i])

print(student_groups)