from django.shortcuts import render, HttpResponse

from .models import ShortenerURL


import random
import string


def code_generator(size=6):
    chars=string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))



def refresh_shortcodes(self):
    qs = ShortenerURL.objects.filter(id__gte=1)
    new_codes = 0
    for q in qs:
        q.shortcode = code_generator()
        q.save()
        new_codes += 1
    return "New codes made: {i}".format(i=new_codes)


def new_shortcode():
    return HttpResponse('ok')
