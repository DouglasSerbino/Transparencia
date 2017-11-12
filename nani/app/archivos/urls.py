from django.conf.urls import url
from django.contrib import admin
from app.archivos import views 

urlpatterns = [
 url(r'^documentos/$', views.documentos, name='principal' ),
 url(r'^documentos/edit/(?P<id_documento>\d+)/$', views.editardocs, name='editar_documentos'),

]