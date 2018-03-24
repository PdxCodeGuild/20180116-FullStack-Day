

# Forms

Let's take a look back at [HTML forms](../../2%20HTML%20+%20CSS/docs/12%20-%20HTML%20Forms.md). You don't have to do anything special to use forms in Django. The `input` elements need `name` attributes, the `action` attribute of the form needs to point to a view. When you submit the data, the form will gather all the `name` attributes from the `input` fields and associate them with each `input`'s `value`.

```html
<form action="{% url 'todoapp:newtodo' %}" method="post">
    {% csrf_token %}
    <input type="text" name="todo_text" value="mytext"/>
    <input type=""
    <button type="submit">add todo</button>
</form>
```

Django will take the name-value pairs from the request and put them into a dictionary-like object `request.POST`. You can then access those values from the view using the `name` as a key.

```python
def newtodo(request):
    todo_text = request.POST['todo_text'] # 'mytext'
    todo = Todo(text=todo_text, completed=False)
    todo.save()
    return HttpResponseRedirect(reverse('todoapp:index'))
```

## The Form Class

Django has a special Form class to make the creation of forms easier. You can read in the official docs: [Working with Forms](https://docs.djangoproject.com/en/2.0/topics/forms/), [Forms API](https://docs.djangoproject.com/en/2.0/ref/forms/api/#django.forms.Form). You can put your forms in `forms.py` inside your app.


##### forms.py
```python
from django import forms
class TodoForm(forms.Form):
    todo_text = forms.CharField(label='Todo Text', max_length=100)
```

##### views.py
```python
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import TodoForm
def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo_text = form.cleaned_data['todo_text']
            todo = Todo(text=todo_text)
            todo.save()
            form = TodoForm() # blank form
        # if the form is invalid, we just send it back to the template
    else:
        form = TodoForm()
    return render(request, 'name.html', {'form': form})
```

##### index.html
```html
<form action="{% url 'todoapp:index' %}" method="post">
    {% csrf_token %}
    {{ form }}
    <input type="submit" value="Submit" />
</form>
```


## The ModelForm Class

ModelForms allow us to generate a form directly from a model. You can read more about ModelForms in the [official docs](https://docs.djangoproject.com/en/2.0/topics/forms/modelforms/).

##### forms.py
```python
from django.forms import ModelForm
from .models import Todo
class TodoForm(ModelForm):
    class Meta:
        # the model to associate with the form
        model = Todo
        # a list of all the models' fields you want in the form
        fields = ['text']
```
