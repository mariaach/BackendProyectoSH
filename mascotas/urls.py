from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_mascotas, name='lista_mascotas'),
    path('nueva/', views.crear_mascota, name='crear_mascota'),
    path('editar/<int:pk>/', views.editar_mascota, name='editar_mascota'),
    path('eliminar/<int:pk>/', views.eliminar_mascota, name='eliminar_mascota'),
]