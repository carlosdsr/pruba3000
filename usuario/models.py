from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    cedula = models.CharField(max_length=50)
    cargo = models.BooleanField(default=True)
    codigoEmpleado = models.CharField(max_length=50)
    intentosInicioSesion = models.IntegerField
