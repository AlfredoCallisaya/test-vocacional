from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class UsuarioPersonalizado(AbstractUser):
    edad = models.PositiveIntegerField(null=True, blank=True)
    ROL_CHOICES = [
        ('admin', 'Administrador'),
        ('usuario', 'Usuario Normal'),
    ]
    rol = models.CharField(max_length=20, choices=[('admin', 'Administrador'), ('user', 'Usuario')], default='user')
    
