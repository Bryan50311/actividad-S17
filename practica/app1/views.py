from django.shortcuts import render, redirect
from .models import Carrera, Estudiante
from .forms import CarreraForm, EstudianteForm


def home(request):
    return render(request, 'home.html')

# LISTA DE CARRERAS
def carreras_lista(request):
    carreras = Carrera.objects.all()
    return render(request, 'carreras.html', {'carreras': carreras})


# CREAR CARRERA
def carrera_nueva(request):
    if request.method == 'POST':
        form = CarreraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carreras_lista')
    else:
        form = CarreraForm()

    return render(request, 'crear_carrera.html', {'form': form})


# LISTA DE ESTUDIANTES
def estudiantes_lista(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes.html', {'estudiantes': estudiantes})


# CREAR ESTUDIANTE
def estudiante_nuevo(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estudiantes_lista')
    else:
        form = EstudianteForm()

    return render(request, 'crear_estudiante.html', {'form': form})
