from django.contrib import admin
from .models import Mascota

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre_masc', 'especie', 'raza', 'edad_masc', 'estado', 'foto_masc')
    list_filter = ('especie', 'estado')
    search_fields = ('nombre_masc', 'raza')

admin.site.register(Mascota, MascotaAdmin)