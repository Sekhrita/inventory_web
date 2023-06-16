from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    run = models.CharField(max_length=20, default='---')
    telefono = models.CharField(max_length=20, default='---')
    direccion = models.CharField(max_length=100, null=True, blank=True, default='---')
    presentacion = models.CharField(max_length=400, null=True, blank=True, default='---')

    imagen = models.ImageField(default='icon_default_user.png', upload_to='users/')