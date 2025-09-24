from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Profesor

# Create your views here.
def matematicas(request):
    context = {
        'numero1': 10,
        'numero2': 5,
        'suma': 10 + 5,
        'resta': 10 - 5,
        'multiplicacion': 10 * 5,
        'division': 10 / 5,
    }
    return render(request, 'matematicas.html', context)

def historia(request):
    return render(request, 'historia.html')

def ciencias(request):
    return render(request, 'ciencias.html')

def lista_profesores(request):
    profesores = Profesor.objects.all()
    context = {'profesores': profesores}
    return render(request, 'lista_profesores.html', context)
