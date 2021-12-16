from django.shortcuts import  render, redirect
from .models import Asignaturas
from .forms import AsignaturasForm

# Create your views here.
def listar_asignaturas(r):
    context = {
        "name" : "Gian",
        "asignaturas": Asignaturas.objects.all() ## traiga todos los registros

    }
    return render(r, "asignaturas/listar.html", context) ## esto carga el html

def crear(r):
    formulario =  AsignaturasForm()
    context = {
        "formulario" :formulario,
        "nombre_boton" : "Crear"
    }

    if r.POST:
        formulario = AsignaturasForm(r.POST)
        formulario.save()

        return redirect("listar")

    return render(r, "asignaturas/crear.html", context)

def actualizar(r,id):
    asignaturas = Asignaturas.objects.get(pk=id) ## traer un solo registro 
    formulario = AsignaturasForm(instance=asignaturas)
    context = {
        "formulario" :formulario,
        "nombre_boton" : "Actualizar"
    }

    if r.POST:
        formulario = AsignaturasForm(r.POST, instance=asignaturas )
        formulario.save()

        return redirect("listar")

    return render(r, "asignaturas/crear.html", context)


def eliminar(r,id):
    if r.POST:
        asignatura = Asignaturas.objects.get(pk=id) ## traer un solo registro 
        asignatura.delete()

        return redirect("listar")

    return render(r, "asignaturas/eliminar.html")