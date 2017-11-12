# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Modelo: Perfil Institucional
# Autor: Kendal Sosa
# Objetivo: Describir las instituciones
class PerfilInstitucion(models.Model):
	nombre = models.CharField(max_length=50)
	abreviatura = models.CharField(max_length=25)
	direccion = models.CharField(max_length=250)
	nit = models.CharField(max_length=14)
	telefono = models.CharField(max_length=8)
	email = models.EmailField()
	web = models.URLField()
	fecha_fundacion = models.DateField(auto_now=False, auto_now_add=False)
	presidente = models.CharField(max_length=50)
	director_institucion = models.CharField(max_length=50)

# Modelo: Usuario
# Autor: Kendal Sosa
# Objetivo: Describir una cuenta de usuario
class Usuario(models.Model):
	nombre = models.CharField(max_length=25)
	correo = models.EmailField()
	institucion = models.OneToOneField(PerfilInstitucion, blank=True, null=True)

# Nombre: Rol
# Autor: Kendal Sosa
# Objetivo: Decribir los roles de los Usuarios
class Rol(models.Model):
	nombre = models.CharField(max_length=30)


# Nombre: Dominio
# Autor: Kendal Sosa
# Objetivo: Definir el dominio de cada institucion
class Dominio(models.Model):
	nombre_dominio = models.CharField(max_length=50)

	def get_dominio(self):
		'''Retorna el dominio al que pertenece un usuario'''
		dominio = None
		if self.nombre_dominio.exists():
			dominio = self.nombre_dominio

		return dominio