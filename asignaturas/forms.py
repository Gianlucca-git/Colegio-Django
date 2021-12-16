from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from django import forms
from .models import Asignaturas

class AsignaturasForm(ModelForm):

    class Meta:
        model = Asignaturas
        fields = '__all__'
        labels = {
            'name':'Nombre Completo',
            'code':'Codigó',
            'credits':'Creditos'
        }