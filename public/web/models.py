from django.db import models


class Destino_tipo(models.Model):
    tipo = models.CharField(max_length=64)

    def __str__(self):
        return self.tipo

class Destino_dificultad(models.Model):
    dificultad = models.CharField(max_length=64)

    def __str__(self):
        return self.dificultad

class Destino(models.Model):
    nombre = models.CharField(max_length=255)
    foto_portada = models.CharField(max_length=255)
    mapa = models.CharField(max_length=512)
    como_llegar = models.TextField()
    descripcion = models.TextField()
    contacto = models.CharField(max_length=255, null=True, blank=True)
    precaucion = models.CharField(max_length=255, null=True, blank=True)
    tipo = models.ForeignKey(Destino_tipo, on_delete=models.SET_NULL, null=True, blank=True)
    dificultad = models.ForeignKey(Destino_dificultad, on_delete=models.SET_NULL, null=True, blank=True)
    duracion = models.CharField(max_length=64, null=True, blank=True)
    distancia = models.CharField(max_length=64, null=True, blank=True)
    desnivel = models.CharField(max_length=64, null=True, blank=True)
    tiempo = models.CharField(max_length=64, null=True, blank=True)

    fecha_creado = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificado = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.nombre

class Album(models.Model):
    destino = models.ForeignKey(Destino, on_delete=models.SET_NULL, null=True, blank=True)
    foto = models.CharField(max_length=512)
    coordenada = models.CharField(max_length=512, null=True, blank=True)
    detalle = models.CharField(max_length=128, null=True, blank=True)
    autor = models.CharField(max_length=64, null=True, blank=True)
    posicion = models.IntegerField(null=True, blank=True)

    fecha_creado = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificado = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.foto