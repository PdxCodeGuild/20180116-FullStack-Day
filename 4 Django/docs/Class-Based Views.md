

# Class-Based Views

- [Reference Documentation](https://docs.djangoproject.com/en/2.0/ref/class-based-views/)
- [Introduction to class-based views](https://docs.djangoproject.com/en/2.0/topics/class-based-views/intro/)
- [Part of the polls tutorial](https://docs.djangoproject.com/en/2.0/intro/tutorial04/#use-generic-views-less-code-is-better)
- [Built-in class-based generic views](https://docs.djangoproject.com/en/2.0/topics/class-based-views/generic-display/)
- [Form handling with class-based views](https://docs.djangoproject.com/en/2.0/topics/class-based-views/generic-editing/)
- [Using mixins with class-based views](https://docs.djangoproject.com/en/2.0/topics/class-based-views/mixins/)


- [simpleisbetterthancomplex.com's overview](https://simpleisbetterthancomplex.com/article/2017/03/21/class-based-views-vs-function-based-views.html)


## Types of Views

- [Base Views: View, TemplateView, RedirectView](https://docs.djangoproject.com/en/2.0/ref/class-based-views/base/)
- [Display Views: DetailView,List View](https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-display/)
- [Editing Views: FormView, CreateView, UpdateView, DeleteView](https://docs.djangoproject.com/en/2.0/ref/class-based-views/generic-editing/)


## Routing

To create a route to a class-based view, you have to call `as_view()` and pass the result to `path`. The `DetailView` requires a `pk` in the path.

```python
from django.urls import path
from . import views
app_name = 'myapp'
urlpatterns = [
    
    # function-based view
    path('', views.index, name='index'),
    path('<int:model_id>/', views.detail, name='detail'),
    
    # class-based view
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail')
]
```

## View

This the the base class of all other class-based views. It allows you to write a method to handle each HTTP method.

```python
# function-based view
def index(request):
    if request.method == 'GET':
        #...
    elif request.method == 'POST':
        #...

# class-based view
from django.views import View
class MyView(View):
    def get(self, request):
        #...
    def post(self, request):
        #...
```

## TemplateView

The `TemplateView` allows you to define a view just by specifying a template name and the data used to render it.

```python
from django.views.generic.base import TemplateView
from .models import MyModel
class MyView(TemplateView):
    template_name = "mytemplate.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_model'] = MyModel.objects.all()
        return context
```

You can actually use a TemplateView without writing your own implementation.

```python
from django.views.generic.base import TemplateView
urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name="home"),
]
```


## ListView

A `ListView` 

The list of objects will default to the name `mymodel_list` in the template. You can customize this by setting `context_object_name` inside your view. You can also filter the data by overriding the `get_queryset` method.

The template used will default to `mymodel_list.html`. You can customize this by specifying a `template_name` inside your view.


```python
from django.views import generic
from .models import MyModel
class MyListView(generic.ListView):
    model = MyModel
    
    #below are default values you can change
    #context_object_name = 'mymodel_list'
    #template_name = 'myapp/mymodel_list.html'
    #def get_queryset(self):
    #    return MyModel.objects.all()
```



## DetailView

DetailView expects a 'pk' in the route: `path('<int:pk>/', views.DetailView.as_view(), name='detail')`.

The object's name will default to the name `mymodel` in the template. You can customize this by setting `context_object_name` inside your view.

The template used will default to `mymodel_detail.html`. You can customize this by specifying a `template_name` inside your view.


```python
from django.views import generic
from .models import MyModel
class MyDetailView(generic.DetailView):
    model = MyModel
    
    #below are default values you can change
    #context_object_name = 'mymodel'
    #template_name = 'myapp/mymodel_detail.html'
    #def get_object(self):
    #   object = super().get_object()
    #   return object
```


