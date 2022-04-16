from django.db import models
from django.forms import CharField

# Create your models here.

class User(models.Model):
    username = CharField(max_length=200)
    email = CharField(max_length=200)
    password = CharField(max_length=200)

    def __str__(self):
        return self.username