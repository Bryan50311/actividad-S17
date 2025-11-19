from django import forms
from .models import Carrera, Estudiante

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['nombre', 'duracion', 'facultad', 'descripcion']


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'edad', 'correo', 'fecha_ingreso', 'carrera']
