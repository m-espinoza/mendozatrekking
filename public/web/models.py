from django.db import models

class Destino(models.Model):
    nombre = models.CharField(max_length=255)
    foto_portada = models.CharField(max_length=255)
    mapa = models.CharField(max_length=512)
    como_llegar = models.TextField()
    descripcion = models.TextField()
    contacto = models.CharField(max_length=255, null=True, blank=True)
    precaucion = models.CharField(max_length=255, null=True, blank=True)

    fecha_creado = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificado = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombre

class Album(models.Model):
    destino = models.ForeignKey(Destino, on_delete=models.CASCADE)
    foto = models.CharField(max_length=512)
    coordenada = models.CharField(max_length=512, null=True, blank=True)
    detalle = models.CharField(max_length=128, null=True, blank=True)
    autor = models.CharField(max_length=128, null=True, blank=True)

    fecha_creado = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificado = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombre
