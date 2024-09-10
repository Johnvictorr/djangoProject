from django.shortcuts import render
from .models import Pessoa

def listarRegistros(request):
    pessoa = Pessoa.objects.all()
    return render(request, 'file.html', {'pessoa': pessoa})