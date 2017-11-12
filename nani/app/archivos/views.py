# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_list_or_404, get_object_or_404

#Decorador de pagina de errores
from django.views.defaults import page_not_found

from django.shortcuts import render
from forms import DocumentoForm
from models import Documento


# Create your views here.
def documentos(request):
	documento = Documento.objects.all()
	if request.method == 'POST':
		form = DocumentoForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return render(request, "Administracion/documentos.html", {'form':form, 'documento':documento})
	else:
		form = DocumentoForm()
	return render(request, "Administracion/documentos.html", {'form':form, 'documento':documento})

def editardocs(request, id_documento):
	documento = get_object_or_404(Documento, id=id_documento)
	form = DocumentoForm(request.POST or None, request.FILES or None, instance=documento)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('archivos:principal'))
	return render(request, 'Administracion/editdocs.html', {'form': form}) 


#Manejo de errores
def error_404(request):
    return render(request, 'Errores/404.html', {}) 

def error_500(request):
	return render(request, 'Errores/500.html', {})