from django.urls import path
from . import views

urlpatterns = [
    path('', views.calcular_nota, name='calcular_nota'),
]
