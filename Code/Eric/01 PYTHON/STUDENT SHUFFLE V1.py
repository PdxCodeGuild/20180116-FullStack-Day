import random

student_list = ['anna', 'brianna', 'colton', 'eric', 'jackson', 'justin', 'maggie', 'matt b',
                'michael m', 'michael g', 'ociel', 'scott', 'sergio', 'wes', 'zixuan']

absentee_list = ['michael g', 'matt b', 'scott']

print(len(student_list))

for i in range(len(absentee_list)):
	student_list.remove(absentee_list[i])

print(student_list)

group_size = 3
number_of_groups = len(student_list)//group_size

student_groups = []
for i in range(number_of_groups):
	student_groups.append([])


# while len(student_list) > 0:
# 	for i in range(number_of_groups):
# 		if len(student_list) == 0:
# 			break
# 		student = student_list.pop(random.randint(0, len(student_list) - 1))
# 		student_groups[i].append(student)
#
# # print(student_groups)
#
#
# index = 0
# while len(student_list) > 0:
# 	student = student_list.pop(random.random.randint (0, len (student_list) - 1))
# 	student_groups[index].append(student)
# 	index += 1
# 	if index == number_of_groups:
# 		index = 0
random.shuffle(student_list)

for i in range(len(student_list)):
	group = i % number_of_groups
	student_groups[group].append(student_list[i])

print(student_groups)
