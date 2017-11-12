# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from forms import DocumentoForm
from models import Documento

# Create your views here.
def documentos(request):
	documento = Documento.objects.all()
	if request.method == 'POST':
		form = DocumentoForm(request.POST)

		if form.is_valid():
			form.save()
		else:
			form = DocumentoForm()
	else:
		form = DocumentoForm()
	return render(request, "Administracion/documentos.html", {'form':form, 'documento':documento})