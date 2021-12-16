from django.shortcuts import redirect, render

from .models import Estudiante , EstudianteAsignatura
from .forms import EstudianteForm , EstudianteAsignaturasForm

# Create your views here.
def principal(r):
    context = {
        "name" : "Gian",
        "estudiantes": Estudiante.objects.all()
    }
    return render(r, "estudiante/listar.html", context)

def crearEstudiante(r):
    formulario =  EstudianteForm()
    context = {
        "formulario" :formulario
    }

    if r.POST:
        formulario = EstudianteForm(r.POST)
        formulario.save()
        
        return redirect('listar')

    return render(r, "estudiante/crear.html", context)

def listarAsignaturas(r, id):
    estudiante = Estudiante.objects.get(pk=id)
    asignaturas = EstudianteAsignatura.objects.filter(estudiante=estudiante) ##regresa el join con la tabla asignatura
    
    context = {  
        "asignaturas" : asignaturas
      }
    return render(r, "estudiante/listar_asignaturas.html", context)

def crearAsignaturas(r):
    formulario = EstudianteAsignaturasForm()
    context = {  
        "formulario" : formulario,
        "nombre_boton" : "Ingresar Matricula" 
      }
    if r.POST:
        formulario = EstudianteAsignaturasForm(r.POST)
        formulario.save()

        return redirect('listar_asignaturas')

    return render(r, "estudiante/crearAsignatura.html", context)
