from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
# Create your models here.

class Cliente(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    identificacion = models.CharField(max_length=11)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    class Meta:
        ordering = ('created',)

admin.site.register(Cliente)