from .models import Evento, Charla, Taller, Conversatorio, JornadaAdopcion  
from django.core.paginator import Paginator
from django.shortcuts import render


def actividades(request):
    eventos_list = Evento.objects.all()
    charlas_list = Charla.objects.all()
    talleres_list = Taller.objects.all()
    conversatorios_list = Conversatorio.objects.all()
    jornadas_adopcion_list = JornadaAdopcion.objects.all()
    
    # Configuración de la paginación
    paginator_eventos = Paginator(eventos_list, 16)  # Muestra 4 eventos por página
    paginator_charlas = Paginator(charlas_list, 16)  # Muestra 4 charlas por página
    paginator_talleres = Paginator(talleres_list, 16)  # Muestra 4 talleres por página
    paginator_conversatorios = Paginator(conversatorios_list, 16)  # Muestra 4 conversatorios por página
    paginator_jornadas = Paginator(jornadas_adopcion_list, 16)  # Muestra 4 jornadas por página
    
    page_number = request.GET.get('page')
    eventos = paginator_eventos.get_page(page_number)
    charlas = paginator_charlas.get_page(page_number)
    talleres = paginator_talleres.get_page(page_number)
    conversatorios = paginator_conversatorios.get_page(page_number)
    jornadas_adopcion = paginator_jornadas.get_page(page_number)
    
    context = {
        'eventos': eventos,
        'charlas': charlas,
        'talleres': talleres,
        'conversatorios': conversatorios,
        'jornadas_adopcion': jornadas_adopcion,
    }
    
    return render(request, 'actividades.html', context)