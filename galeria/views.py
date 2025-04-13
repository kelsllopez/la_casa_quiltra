from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Galeria

def uwu(request):
    fotos_list = Galeria.objects.all()  # Obtener todas las galerías
    paginator = Paginator(fotos_list, 16)  # Muestra 6 elementos por página
    page = request.GET.get('page')
    fotos = paginator.get_page(page)

    context = {
        'fotos': fotos,
    }
    return render(request, 'e.html', context)
