jackalopes = [0 , 0]
year = 0

while len(jackalopes) < 1000:
    pair_count = 0
    year += 1
    for i in range(len())


########

'''
import random


def make_jacklope():
  names = ['mike', 'vere', 'marcy', 'kim', 'joy', 'mildred', 'marty', 'Jeff', 'Manny', 'megan', 'mad max', 'Moore', 'junior', 'Minty', 'myspace tom', 'Hugh Jass', 'john', 'jacob', 'jingleheimer', 'smith' 'Morticia', 'Rick', 'Morty',  'jon smith', 'not sure', 'Mob', 'Toffle', 'moore']
  jack_name = random.choice(names)
  age = 0
  sex = random.choice(['male', 'female'])
  pregnant = False
  return {'name': jack_name, 'age': age, 'sex': sex, 'pregnant': pregnant}
  

for i in range(10):
  print(make_jacklope)
  '''
'''
import random

def make_jackalope():
  names = ['mike', 'vere', 'marcy', 'kim', 'joy', 'mildred', 'marty', 'Jeff', 'Manny', 'megan', 'mad max', 'Moore', 'junior', 'Minty', 'myspace tom', 'Hugh Jass', 'john', 'jacob', 'jingleheimer', 'smith', 'Morticia', 'Rick', 'Morty',  'jon smith', 'not sure', 'Beef Supreme', 'Mob', 'Toffle', 'moore']
  jack_name = random.choice(names)
  age = 0
  sex = random.choice(['male', 'female'])
  pregnant = False
  return {'name': jack_name, 'age': age, 'sex': sex, 'pregnant': pregnant}
  
population = [make_jackalope(), make_jackalope()]

population[0]['sex'] = 'male'
population[1]['sex'] = 'female'

                 

for year in range(100):
	random.shuffle(population)
	for i in range(len(population) - 1):
  	j1 = population[i]
    j2 = population[i + 1]
    if j1['sex'] != j2['sex'] and 4 < j1['age'] < 9 and 4 < j2['age'] < 9 and j1['pregnant'] != True and j2['pregnant'] != True :
      if j1['sex'] = 'female':
        j1['pregnant'] = True
        
      else: 
        j2['pregnant'] = True
      	
      
      j3 = make_jackalope()
      j3['name'] = j1['name'] + '-' + j2['name']
      population.append(j3)
        
if jackalope.pull_out() == False:
  jackalope.plan_b()
'''
'''
import random

def make_jackalope():
  names = ['mike', 'vere', 'marcy', 'kim', 'joy', 'mildred', 'marty', 'Jeff', 'Manny', 'megan', 'mad max', 'Moore', 'junior', 'Minty', 'myspace tom', 'Hugh Jass', 'john', 'jacob', 'jingleheimer', 'smith', 'Morticia', 'Rick', 'Morty',  'jon smith', 'not sure', 'Beef Supreme', 'Mob', 'Toffle', 'moore']
  jack_name = random.choice(names)
  age = 0
  sex = random.choice(['male', 'female'])
  pregnant = False
  return {'name': jack_name, 'age': age, 'sex': sex, 'pregnant': pregnant}


# inititalize our booming population (baby boomers) initialize wreck economy and x.blame(lazy_millenials)
population = [make_jackalope(), make_jackalope()]
population[0]['sex'] = 'male'
population[1]['sex'] = 'female'

for year in range(100): # go through 100 long years of solitude
	random.shuffle(population)
	for i in range(len(population) - 1):
  	j1 = population[i]
    j2 = population[i + 1]
    if j1['pregnant'] or j2['pregnant']: #buy balloons assign.blame(new_generation) #buy avocados with mortgage
      j3 = make_jackalope()
      j3['name'] = j1['name'] + '-' + j2['name']
      population.append(j3)
      j1['pregnant'] = False
      j2['pregnant'] = False
    if j1['sex'] != j2['sex'] and 4 < j1['age'] < 9 and 4 < j2['age'] < 9 and not j1['pregnant'] and not j2['pregnant']:
      if j1['sex'] == 'female':
        j1['pregnant'] = True
      else: 
        j2['pregnant'] = True
    break

'''
'''
import random

def make_jackalope():
  names = ['mike', 'vere', 'marcy', 'kim', 'joy', 'mildred', 'marty', 'Jeff', 'Manny', 'megan', 'mad max', 'Moore', 'junior', 'Minty', 'myspace tom', 'Hugh Jass', 'john', 'jacob', 'jingleheimer', 'smith', 'Morticia', 'Rick', 'Morty',  'jon smith', 'not sure', 'Beef Supreme', 'Mob', 'Toffle', 'moore']
  jack_name = random.choice(names)
  age = 0
  sex = random.choice(['male', 'female'])
  pregnant = False
  return {'name': jack_name, 'age': age, 'sex': sex, 'pregnant': pregnant}


# inititalize our booming population (baby boomers) initialize wreck economy and x.blame(lazy_millenials)
population = [make_jackalope(), make_jackalope()]
population[0]['sex'] = 'male'
population[1]['sex'] = 'female'

for year in range(10): # go through 10 long years of solitude from tinder import Match-Group import grindr import bumble
	random.shuffle(population)
	for i in range(len(population) - 1):
  	j1 = population[i]
    j2 = population[i + 1]
    if j1['pregnant'] or j2['pregnant']: #buy balloons assign.blame(new_generation) #buy non gmo, gluten free extra vegan avocados with re-financing mortgage
      j3 = make_jackalope()
      j3['name'] = j1['name'] + '-' + j2['name']
      population.append(j3)
      j1['pregnant'] = False#phew
      j2['pregnant'] = False
    if j1['sex'] != j2['sex'] and 4 < j1['age'] < 9 and 4 < j2['age'] < 9 and not j1['pregnant'] and not j2['pregnant']:
      if j1['sex'] == 'female':
        j1['pregnant'] = True
      else: 
        j2['pregnant'] = True
    j1['age'] += 1 
		if j1['age'] == 10:		# sad faces *sobbing* #cause of death = stress of life or nuclear war with north jackaloporea or russia hack election. 10 year old Jackalopes are delicious.
      population.pop(i)		# RIP

for jackalope in population:
  print(jackalope['name'])
  print(f'\tage: {jacaklope["age"]}')
  print(f'\tage: {jacaklope["sex"]}')
  print(f'\tage: {jacaklope["pregnant"]}')
'''