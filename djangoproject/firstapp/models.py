from django.db import models

# Create your models here.
'''
A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you're storing. ... Each attribute of the model represents a database field. With all of this, Django gives you an automatically-generated database-access API
'''
class Firstapp(models.Model):
    name = models.ChartField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
