from django.db import models

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.TextField()
    telefono = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)
