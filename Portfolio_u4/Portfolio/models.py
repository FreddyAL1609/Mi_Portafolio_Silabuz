from django.conf import settings
from django.db import models

# Create your models here.
class portafolio(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    foto = models.URLField(max_length=100)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=100)
    etiqueta = models.CharField(max_length=50)
    url = models.URLField(max_length=100)

    def __str__(self):
        return self.titulo

class ips(models.Model):
    ip = models.CharField(max_length=50)
    enrutable = models.CharField(max_length=50)

    def __str__(self):
        return self.ip



