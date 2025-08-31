from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from .models import Mascota
from .forms import MascotaForm

def lista_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascotas/lista.html', {'mascotas': mascotas})

def lista_mascotas_json(request):
    mascotas = Mascota.objects.all().values()
    return JsonResponse(list(mascotas), safe=False)

def crear_mascota(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_mascotas')
    else:
        form = MascotaForm()
    return render(request, 'mascotas/form.html', {'form': form})

def editar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        if form.is_valid():
            form.save()
            return redirect('lista_mascotas')
    else:
        form = MascotaForm(instance=mascota)
    return render(request, 'mascotas/form.html', {'form': form})

def eliminar_mascota(request, pk):
    mascota = get_object_or_404(Mascota, pk=pk)
    if request.method == 'POST':
        mascota.delete()
        return redirect('lista_mascotas')
    return render(request, 'mascotas/confirmar_eliminar.html', {'mascota': mascota})

def inicio(request):
    return render(request, 'mascotas/inicio.html')

# ✅ Nueva función para recibir JSON desde Postman
@csrf_exempt  # Evita error CSRF en pruebas con Postman
def crear_mascota_json(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            mascota = Mascota.objects.create(**data)
            return JsonResponse({"message": "Mascota creada con éxito", "id": mascota.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)
