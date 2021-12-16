from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.

class Asignaturas(models.Model):
    name = CharField(max_length=100)
    code = IntegerField ()
    credits = IntegerField (default= 4)

    def __str__(self):
        return self.name 
