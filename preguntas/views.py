from django.shortcuts import render
from .models import Pregunta

def preguntas_view(request):
    preguntas = Pregunta.objects.all()
    return render(request, 'preguntas.html', {'preguntas': preguntas})
