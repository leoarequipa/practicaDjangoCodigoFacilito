from django.db import models
from apps.adopcion.models import Persona
# Create your models here.

class Vacuna(models.Model):
    nombre = models.CharField(max_length = 10, primary_key = True, default="")

    def __str__(self):
        return '{}'.format(self.nombre)
    
class Mascota(models.Model):
    folio = models.CharField(max_length = 10, primary_key = True, default="")
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    persona = models.ForeignKey(Persona, null = True, blank = True, on_delete=models.CASCADE)
    vacunas = models.ManyToManyField(Vacuna, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)
