from django.urls import path 
from . import views

urlpatterns = [
    path('listar', views.listar_asignaturas, name="listar"),
    path('crear', views.crear, name="crear"),
    path('actualizar/<int:id>', views.actualizar, name="actualizar"),
    path('eliminar/<int:id>', views.eliminar, name="eliminar")
]