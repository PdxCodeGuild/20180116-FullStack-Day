import random

student_list = ['Justin', 'Jackson', 'Anna', 'Brianna', 'Maggie', 'Colton', 'Wes', 'Zixuan', 'OCL', 'Sergio', 'Eric', 'Michael M', 'Matt', 'Michael G']

absent_student_list = []


for i in range(len(absent_student_list)):
    student_list.remove(absent_student_list[i])

print(student_list)

# group_size = int(input('Size of group?'))
group_size = 3
number_of_groups = len(student_list) // group_size


# student_groups = [['Justin', 'Jackson', 'Anna'],
#                   ['Brianna', 'Maggie', 'Colton'],
#                   ['Wes', 'Zixuan', 'OCL',],
#                   ['Sergio', 'Eric', 'Michael M']]
#




#student_groups = [[]]*number_of_groups

student_groups = []
for i in range(number_of_groups):
    student_groups.append([])


# while len(student_list) > 0:
#     for i in range(number_of_groups):
#         if len(student_list) == 0:
#             break
#         student = student_list.pop(random.randint(0, len(student_list)-1))
#         student_groups[i].append(student)
# print(student_groups)
#
#
# index = 0
# while len(student_list) > 0:
#     student = student_list.pop(random.randint(0, len(student_list) - 1))
#     student_groups[index].append(student)
#     index += 1
#     if index == number_of_groups:
#         index = 0
# print(student_groups)
#

random.shuffle(student_list)

for i in range(len(student_list)):
    group = i % number_of_groups
    #print(f'{i}%{number_of_groups}={i%number_of_groups}')
    student_groups[group].append(student_list[i])

print(student_groups)





