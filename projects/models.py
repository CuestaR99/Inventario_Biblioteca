from django.db import models

# Create your models here.
class Libros(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    ano_publicacion = models.CharField(max_length=4)
    mes_publicacion = models.CharField(max_length=50, null=True, blank=True)
    dia_publicacion = models.IntegerField()
    genero = models.CharField(max_length=100)
