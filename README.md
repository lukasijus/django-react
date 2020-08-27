#Create django and react project from scratch

Launch python virtual environmnet
```bash
pipenv shell
```

Install django dependencies
```bash
pipenv install django djangorestframework django-rest-knox
```
Start a django project
```bash
django-admin startproject djangoproject
```

Your directory should look something like this
```bash
|   Pipfile
|   Pipfile.lock
|   README.md
|
\---djangoproject
    |   manage.py
    |
    \---djangoproject
            asgi.py
            settings.py
            urls.py
            wsgi.py
            __init__.py
```

Start a django app
```bash
python manage.py startapp firstapp
```

Now the base directory should look like this with djangoproject and firstapp installed
```bash
|   Pipfile
|   Pipfile.lock
|   README.md
|
\---djangoproject
    |   manage.py
    |
    +---djangoproject
    |   |   asgi.py
    |   |   settings.py
    |   |   urls.py
    |   |   wsgi.py
    |   |   __init__.py
    |   |
    |   \---__pycache__
    |           settings.cpython-38.pyc
    |           __init__.cpython-38.pyc
    |
    \---firstapp
        |   admin.py
        |   apps.py
        |   models.py
        |   tests.py
        |   views.py
        |   __init__.py
        |
        \---migrations
                __init__.py```
```

Got to djangoproject/djangoproject/settings.py and add lines to the INSTALLED_APPS sections
```python
INSTALLED_APPS = [
'django.contrib.admin',                                                                                                                                      
'django.contrib.auth',                                                                                                                                       
'django.contrib.contenttypes',                                                                                                                               
'django.contrib.sessions',                                                                                                                                  
'django.contrib.messages',                                                                                                                                   
'django.contrib.staticfiles',                                                                                                                               
'firstapp',                                                                                                                                                  
'rest-framework',                                                                                                                                        
]                                                                                                                                                              
```

Define a model ( a kind of data ) in the firstapp\models.py
```python
from django.db import models

class Firstapp(models.Model):
    name = models.ChartField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
```