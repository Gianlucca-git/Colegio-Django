from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from .models import Estudiante, EstudianteAsignatura

class EstudianteForm(ModelForm):

    class Meta:
        model = Estudiante
        fields = '__all__'
        labels = {
            'name':'Nombre Completo',
            'code':'Codigó',
            'yearOld':'Edad',
            'city':'Ciudad',
            'activate':'Activo'
        }

class EstudianteAsignaturasForm(ModelForm):

    class Meta:
        model = EstudianteAsignatura
        fields = '__all__'
        labels = {
            'estudiante':'Nombre Estudiante',
            'asignatura':'Asignatura'
        }