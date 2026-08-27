from django.db import models


class Producto(models.Model):
    CATEGORIA_CHOICES = [
        ('electronica', 'Electrónica'),
        ('ropa', 'Ropa'),
        ('hogar', 'Hogar'),
    ]

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    fecha_ingreso = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre
