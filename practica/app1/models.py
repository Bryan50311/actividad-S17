from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    duracion = models.IntegerField(help_text="Duración en años")
    facultad = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    correo = models.EmailField()
    fecha_ingreso = models.DateField()
    carrera = models.ForeignKey(Carrera, on_delete=models.CASCADE, default=1)


    def __str__(self):
        return f"Nombre del estudiante: {self.nombre} {self.apellido}"
