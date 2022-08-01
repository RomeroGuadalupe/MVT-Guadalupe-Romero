from asyncio.windows_events import NULL
from django.db import models
from datetime import datetime

# Create your models here.

class familia (models.Model):
    nombre = models.CharField (max_length=40)
    apellido = models.CharField (max_length=40)
    edad = models.IntegerField ()
    fecha_nacimiento = models.DateField(default=datetime.now())
    parentesco = models.CharField(max_length=40, default=NULL)
 