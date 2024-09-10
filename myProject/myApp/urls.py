from django.urls import path
from .views import listarRegistros

urlpatterns = [
    path('listarRegistros', listarRegistros, name='listarRegistros'),
]
