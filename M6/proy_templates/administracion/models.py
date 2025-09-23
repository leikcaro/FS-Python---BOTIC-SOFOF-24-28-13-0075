from django.db import models
from pruebas.models import Estudiante
# Create your models here.

class Factura(models.Model):
    numero = models.CharField(max_length=20)
    fecha = models.DateField()
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Factura {self.numero} - {self.cliente}"