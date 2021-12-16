from django.db import models
from django.db.models.fields import BooleanField, CharField, IntegerField
from asignaturas.models import Asignaturas

# Create your models here. Cada clase es una tabla :3 luego registrarlo en el admin

class Estudiante(models.Model):  
    name = CharField(max_length=100)
    code = IntegerField ()
    yeardOld = IntegerField (default=15)
    city = CharField (max_length=100, default="Tuluá")
    activate = BooleanField (default=True)

    def __str__(self):
        return self.name

class EstudianteAsignatura (models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignaturas, on_delete=models.CASCADE)

    def __str__(self):
        return self.estudiante.name + " / " + self.asignatura.name