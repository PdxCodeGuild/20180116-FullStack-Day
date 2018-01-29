import random


def make_jackalope():
    names = ['mike', 'vere', 'marcy', 'kim', 'joy', 'mildred', 'marty', 'Jeff', 'Manny', 'megan', 'mad max', 'Moore',
             'junior', 'Minty', 'myspace tom', 'Hugh Jass', 'john', 'jacob', 'jingleheimer', 'smith', 'Morticia',
             'Rick', 'Morty', 'jon smith', 'not sure', 'Beef Supreme', 'Mob', 'Toffle', 'moore']
    jack_name = random.choice(names)
    age = 0
    sex = random.choice(['male', 'female'])
    pregnant = False
    return {'name': jack_name, 'age': age, 'sex': sex, 'pregnant': pregnant}


def breed(j1, j2):
    print(j1['name'] + ' mated with ' + j2['name'] + '!')
    j3 = make_jackalope()
    j4 = make_jackalope()
    #j3['name'] = j1['name'] + '-' + j2['name']
    #j4['name'] = j1['name'] + '-' + j2['name']
    print(j3['name'] + ' was born!')
    print(j4['name'] + ' was born!')
    j1['pregnant'] = False  # phew
    j2['pregnant'] = False
    return j3, j4


# inititalize our booming population (baby boomers) initialize wreck economy and x.blame(lazy_millenials)
population = [make_jackalope(), make_jackalope()]
population[0]['sex'] = 'male'
population[1]['sex'] = 'female'

for year in range(100):  # go through 10 long years of solitude from tinder import Match-Group import grindr import bumble
    random.shuffle(population)
    for i in range(len(population) - 1):
        j1 = population[i]
        j2 = population[i + 1]
        if j1['pregnant'] or j2['pregnant']:  # buy balloons assign.blame(new_generation) #buy non gmo, gluten free extra vegan avocados with re-financing mortgage
            population.extend(breed(j1, j2))
        if j1['sex'] != j2['sex'] and 4 < j1['age'] < 9 and 4 < j2['age'] < 9 and not j1['pregnant'] and not j2['pregnant']:
            if j1['sex'] == 'female':
                j1['pregnant'] = True
            else:
                j2['pregnant'] = True

    next_generation = []
    for i in range(len(population)):
        j1 = population[i]
        j1['age'] += 1
        if j1['age'] < 10:
            next_generation.append(j1)
        else:
            print(j1['name'] + ' has died! :[')
    population = next_generation

for jackalope in population:
    print(jackalope['name'])
    print(f'\tage: {jackalope["age"]}')
    print(f'\tsex: {jackalope["sex"]}')
    print(f'\tpregnant: {jackalope["pregnant"]}')
print(len(population))