from django.db import models

# Create your models here.
class Libro(models.Model):
    
    nombre = models.CharField(max_length= 55)
    editorial = models.CharField(max_length= 65)
    nro_paginas = models.IntegerField()
    anio_publicacion = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} - {self.editorial}'
    