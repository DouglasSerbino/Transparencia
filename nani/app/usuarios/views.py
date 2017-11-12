# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Importando modelos
from .models import Usuario

# Importando modelo serializado
from .serializers import UsuarioSerializer

# Importando librerias para RestFramework
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.

# Vista que serializa los usuarios
class UsuarioList(generics.ListCreateAPIView):
	queryset = Usuario.objects.all()
	serializer_class = UsuarioSerializer

	def List(self, request, *args, **kwargs):
		self.object_list = self.filter_queryset(self.get_queryset())
		serializer = self.get_serializer(self.object_list, many=True)
		return Response({'Usuarios': serializer.data})

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Dato.objects.all()
	serializer_class = DatoSerializer

