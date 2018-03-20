from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import MadLib, MadLibWord, MadLibWordType
import random

def index(request):

    # madlib = MadLib.objects.get(name='Fresh Prince')
    # output = madlib.body
    # for madlibword in madlib.madlibword_set.all():
    #     random_word = ''.join([random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(10)])
    #     output = output.replace('{'+madlibword.name+'}', random_word)
    # return HttpResponse('<pre>'+output+'</pre>')

    madlibs = MadLib.objects.all()
    context = {'madlibs': madlibs}
    return render(request, 'madlibapp/index.html', context)




def detail(request, madlib_id):
    #madlib = MadLib.objects.get(pk=madlib_id)
    madlib = get_object_or_404(MadLib, pk=madlib_id)
    return render(request, 'madlibapp/detail.html', {'madlib':madlib})



def generate(request, madlib_id):

    madlib = MadLib.objects.get(pk=madlib_id)
    output = madlib.body
    for madlibword in madlib.madlibword_set.all():
        value = request.POST[madlibword.name]
        output = output.replace('{' + madlibword.name + '}', value)

    return HttpResponse('<pre>'+output+'</pre>')




