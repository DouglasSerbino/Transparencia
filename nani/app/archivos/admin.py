# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Documento

# Register your models here.

class DocumentoAdmin(admin.ModelAdmin):
	list_display=('nombre_documento','archivo')
	# def has_add_permission(self, request):
	# 	return False

	# def get_actions(self, request):
	# 	actions = super(DocumentoAdmin, self).get_actions(request)
	# 	del actions['delete_selected'] 
	# 	return actions

	# def has_delete_permission(self, request, obj=None):
	# 	return False

admin.site.register(Documento,DocumentoAdmin)