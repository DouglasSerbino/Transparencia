# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def documentos(request):
	return render(request, "Administracion/documentos.html", {})