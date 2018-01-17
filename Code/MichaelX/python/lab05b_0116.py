import random



def rando():
    eye = [';', ':', '8', 'E', '>']
    nose = ['^', '-', '>', '@', '7']
    mouth = [')', '/', 'D', 'O', 'P']

    eyes = random.choice(eye)
    noses = random.choice(nose)
    mouths = random.choice(mouth)

    faces = [eyes, noses, mouths]

    while faces < 5:
        faces += 1
        print(faces)



rando()

