with open('contacts_csv.csv', 'r') as file:
	lines = file.read().lower().split('\n')

contact_list = []

for l in lines[1:]:
	contacts = {}
	l = l.split(',')
	contacts['name'] = l[0]
	contacts['fav_fruit'] = l[1]
	contacts['fav_color'] = l[2]
	contact_list.append(contacts)

contact_num = 0
for c in contact_list:
	contact_num += 1
	print(f'CONTACT {contact_num}:\n{c}\n')
