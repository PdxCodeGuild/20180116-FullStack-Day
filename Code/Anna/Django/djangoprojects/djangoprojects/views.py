from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     return HttpResponse('''
#     <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
#     <div class="jumbotron">
#     <div class="container">
#     <h1>Choose an app: </h1>
#         <ul>
#             <li><a href="/polls">Polls App</a></li>
#             <li><a href="/todo">ToDo App</a></li>
#             <li><a href="/shorty">URL Shortener App</a></li>
#         </ul>
#     </div>
#     </div>
#         ''')


def index(request):
    return render(request, 'index.html')
