from django.urls import path
from . import views
app_name = 'encuesta'

urlpatterns = [
    path('', views.index, name='index'),
    path('enviar', views.enviar, name='enviar'),

    path('calculo', views.calculo, name='calculo'),  
    path('resultado', views.resultado, name='resultado'),

    path('cilindro/', views.cilindro, name='cilindro'), 
    path('calcular_volumen/', views.calcular_volumen, name='calcular_volumen'),
]