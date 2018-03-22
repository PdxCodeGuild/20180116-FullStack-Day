# Django Quickstart


## Create a Project and App

- Create a site/project: `django-admin startproject <site/project name>`
- Move into the site's directory: `cd <site/project name>`
- Run migrations to create the database and user system `python manage.py migrate`
- Create an admin account with `python manage.py createsuperuser`, and enter a username, email address, and password

## Create an App

- Create an app: `python manage.py startapp <app-name>`
- Add your app (`appname.apps.AppnameConfig`) to the `INSTALLED_APPS` in `settings.py`

## Create a View

- In your app's `views.py` create a function `def <viewname>(request):`. To test it, you can just `return HttpResponse('ok')`.

## Create a Route to the View

- Create a `urls.py` inside your app
- Add a route in your app's `urls.py` which points to the the view
- Add an `app_name` to be able to look up paths when you render a template

```python
from django.conf.urls import url
from . import views

app_name = '<app name>'
urlpatterns = [
    path('<path>', views.<viewname>, name='<viewname>')
]
```

- Add a route in your project's `urls.py` which points to the app's `url.py` using `include`

```python
from django.conf.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<path>/', include('<appname>.urls'))
]
```

At this point, you should run the server (`python manage.py runserver`) and go to `localhost:8000/app_path/view_path` and verify that you can access the view.

## Create Models

- Define your models (Python classes) in the app's `models.py`
- Stage your migrations: `python manage.py makemigrations <appname>`
- (optional) View the SQL commands that will occur during migrations: `python manage.py sqlmigrate <appname> <migration number>`. You can find the migration number and the code that'll be executed during the migration in `<appname>/migrations/<migration number>_initial.py`
- Perform migrations (synchronize your models with your database): `python manage.py migrate`

## Add the Model to the Admin Panel

- Add a `def __str__(self):` to your model so the admin interface knows how to display it.
- Make your app visible in the admin panel by registering your models with our app's `admin.py`

```python
from django.contrib import admin
from .models import <model name 1> <model name 2>
admin.site.register(<model name 1>)
admin.site.register(<model name 2>)
```

- Go to `localhost:8000/admin` in your browser, and add some data.


## Create a Template

- Create a folder inside you app called `templates`, inside of that create another folder with the name of your app, and inside of *that* create a `<filename>.html`. You can view examples of the template syntax [here](03%20-%20Templates.md).

## Render a Template

- Inside your view, you can use the `render` shortcut to render a template. The first parameter is the request, the second parameter is the name of the template, and the third is a dictionary containing the values you'd like to render in the template.

```python
from django.shortcuts import render
def <view name>(request):
    context = {<name-value pairs>}
    return render(request, '<app name>/<template name>.html', context)
```