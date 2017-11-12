# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Importando Modelos
from models import PerfilInstitucion, Usuario, Dominio, Rol

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Rol)
admin.site.register(Dominio)
admin.site.register(PerfilInstitucion)