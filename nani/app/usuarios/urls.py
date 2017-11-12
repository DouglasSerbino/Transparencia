from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from app.usuarios import views
from django.contrib import admin

urlpatterns = [
	# url(r'^usuarios/$', views.UsuarioList.as_view()),
	# Terminar URLs para enviar datos en RestFramework
	# url(r'^usuarios/(?P<pk>[0-9]+)/$',views.UsuarioDetail.as_view())
]