from django.contrib import admin
from .models import Estudiante, EstudianteAsignatura

# Register your models here.                          luego migrar
admin.site.register(Estudiante)
admin.site.register(EstudianteAsignatura)