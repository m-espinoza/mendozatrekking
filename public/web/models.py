from django.db import models

class sendero(models.Model):
    nombre = models.CharField(max_length=255)
    foto_portada = models.CharField(max_length=255)
    mapa = models.CharField(max_length=512)
