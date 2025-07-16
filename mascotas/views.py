from django.shortcuts import render, redirect, get_object_or_404
from .models import Mascota
from .forms import MascotaForm

def lista_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'mascotas/lista.html', {'mascotas': mascotas})

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