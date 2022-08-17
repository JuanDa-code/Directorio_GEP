from tabnanny import verbose
from django.db import models
from .choices import *

class Usuario(models.Model):
    primer_nombre = models.TextField(verbose_name='Primer Nombre')
    segundo_nombre = models.TextField(verbose_name='Segundo Nombre')
    primer_apellido = models.TextField(verbose_name='Primer Apellido')
    segundo_apellido = models.TextField(verbose_name='Segundo Apellido')
    edad = models.PositiveIntegerField(verbose_name='Edad', null=True, blank=True)
    genero = models.TextField(choices=GENERO_CHOICES, verbose_name='Genero')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento', null=True, blank=True)
    estado = models.BooleanField(default=True, verbose_name='Estado')

    def __str__(self):
        return self.primer_nombre + self.primer_apellido

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['id']

class Directorio(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    ext = models.IntegerField(verbose_name='Extensión')
    email = models.EmailField(verbose_name='Correo Electrónico')
    estado = models.BooleanField(verbose_name='Estado', default=True)

    def __str__(self):
        return self.usuario.primer_nombre + self.usuario.primer_apellido