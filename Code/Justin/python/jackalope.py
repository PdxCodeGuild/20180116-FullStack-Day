import random

population = []
years = 50

# First 2 Jackalopes
population.append({'number': 1, 'age': 0, 'sex': 'male', 'pregnant': 'no', 'alive': 'yes'})
population.append({'number': 2, 'age': 0, 'sex': 'female', 'pregnant': 'no', 'alive': 'yes'})

for i in range(years):

    random.shuffle(population)

    # Pregnant Jackalopes Give Birth
    for i in range(len(population)):
        if population[i]['pregnant'] == 'yes':
            baby = {'number': len(population) + 1, 'age': 0, 'sex': random.choice(['male', 'female']),\
                                    'pregnant': 'no', 'alive': 'yes'}
            print(f'Jackalope {population[i]["number"]} gave birth to a {baby["sex"]} number {baby["number"]}.')
            population.append(baby)
            population[i]['pregnant'] = 'no'


    # Impregnaate Jackalopes
    if len(population) == 2 and population[0]['age'] == 3:
        for i in range(2):
            if population[i]['sex'] == 'female':
                population[i]['pregnant'] = 'yes'
                print(f'Jackalope {population[i]["number"]} is pregnant!')

    for i in range(1, len(population)-1):
        if population[i]['sex'] == 'female' and 3 <= population[i]['age'] <= 8:
            if population[i-1]['sex'] == 'male' and 3 <= population[i-1]['age'] <= 8:
                population[i]['pregnant'] = 'yes'
                print(f'Jackalope {population[i-1]["number"]} impregnanted Jackalope {population[i]["number"]}')
            elif population[i+1]['sex'] == 'male' and 3 <= population[i+1]['age'] <= 8:
                population[i]['pregnant'] = 'yes'
                print(f'Jackalope {population[i+1]["number"]} impregnanted Jackalope {population[i]["number"]}')

    #increment age
    for i in range(len(population)):
        population[i]['age'] += 1
        if population[i]['age'] == 10:
            population[i]['alive'] = 'dead'
            print(f'Jackalope {population[i]["number"]} has died')

    print('*' * 100)


for i in range(len(population)):
    print(population[i])