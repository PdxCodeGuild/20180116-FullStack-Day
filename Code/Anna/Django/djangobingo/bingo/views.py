from django.shortcuts import render
from .models import BingoBox
import random

'''
from django.shortcuts import render
def <view name>(request):
    context = {<name-value pairs>}
    return render(request, '<app name>/<template name>.html', context)
'''


# Create your views here.
def index(request):
    bingo_list = []
    random_bingo_list = []
    for o in BingoBox.objects.all():
        bingo_list.append(o.name)
    # get first half of random list
    while len(random_bingo_list) < 12:
        get_word = random.choice(bingo_list)
        if get_word not in random_bingo_list:
            random_bingo_list.append(get_word)
    # append middle square
    random_bingo_list.append("DJANGO!")
    # get second half of random list
    while len(random_bingo_list) < 25:
        get_word = random.choice(bingo_list)
        if get_word not in random_bingo_list:
            random_bingo_list.append(get_word)
    context = {'bingo_list': random_bingo_list}
    return render(request, 'bingo/index.html', context)


def choose_random():
    pass
