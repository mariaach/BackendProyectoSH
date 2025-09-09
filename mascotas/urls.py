from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lista/', views.lista_mascotas, name='lista_mascotas'),
    path('json/', views.lista_mascotas_json, name='lista_mascotas_json'),
    path('crear/', views.crear_mascota, name='crear_mascota'),
    path('crear-json/', views.crear_mascota_json, name='crear_mascota_json'),  # ✅ Para pruebas en Postman
    path('editar/<int:pk>/', views.editar_mascota, name='editar_mascota'),
    path('eliminar/<int:pk>/', views.eliminar_mascota, name='eliminar_mascota'),
]


# Cambiar los textos del admin
admin.site.site_header = "Administración de Mascotas Fundación Salvando Huellas"
admin.site.site_title = "Panel de Mascotas"
admin.site.index_title = "Bienvenido al portal de gestión"