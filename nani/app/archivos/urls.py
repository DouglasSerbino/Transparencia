from django.conf.urls import url
from django.contrib import admin
from app.archivos import views 

urlpatterns = [
 url(r'^documentos/', views.documentos ),
]