from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
     path('',views.home,name="home"),

    # CARRERAS
    path('carreras/', views.carreras_lista, name="carreras_lista"),
    path('carreras/nueva/', views.carrera_nueva, name="carrera_nueva"),

    # ESTUDIANTES
    path('estudiantes/', views.estudiantes_lista, name="estudiantes_lista"),
    path('estudiantes/nuevo/', views.estudiante_nuevo, name="estudiante_nuevo"),
]
