from django.shortcuts import render, redirect
from .models import *
from nosotros.models import * 
from actividades.models import * 
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect, render
import threading

# Función para enviar el correo en segundo plano
def enviar_correo_async(asunto, cuerpo_mensaje, destinatario):
    send_mail(
        subject=asunto,
        message=cuerpo_mensaje,
        from_email='kelsregla@gmail.com',
        recipient_list=[destinatario],
        fail_silently=False,
    )

def index(request):
    especies_con_animales = Especie.objects.filter(animal__isnull=False).distinct()
    animales = Animal.objects.all()

    # Obtener la información de 'Sobre Nosotros' y 'Informacion Contacto'
    sobre_nosotros = SobreNosotros.objects.first()
    informacion_contacto = InformacionContacto.objects.first()

    # Procesar el formulario de contacto si es un POST
    if request.method == "POST":
        nombre = request.POST.get("name")
        email = request.POST.get("email")
        asunto = request.POST.get("subject")
        mensaje = request.POST.get("message")

        if nombre and email and asunto and mensaje:
            # Guardar el mensaje en la base de datos
            MensajeContacto.objects.create(
                nombre_usuario=nombre,
                email_usuario=email,
                asunto=asunto,
                mensaje=mensaje
            )
            
            # Preparar el cuerpo del correo
            cuerpo_mensaje = f"""
            Nuevo mensaje desde el formulario de contacto:

            Nombre: {nombre}
            Email: {email}
            Asunto: {asunto}
            Mensaje:
            {mensaje}
            """

            # Enviar el correo en un hilo separado
            asunto_email = f"📥 Nuevo mensaje: {asunto}"
            thread = threading.Thread(
                target=enviar_correo_async,
                args=(asunto_email, cuerpo_mensaje, 'kelsregla@gmail.com')
            )
            thread.daemon = True  # El hilo se cerrará cuando el programa principal termine
            thread.start()
            
            messages.success(request, "Tu mensaje ha sido enviado con éxito.")
            return redirect("contacto")  # Redirige a la página de contacto después de enviar el mensaje
        else:
            messages.error(request, "Todos los campos son obligatorios.")

    # Pasar al contexto la información relevante
    context = {
        'animales': animales,
        'sobre_nosotros': sobre_nosotros,
        'informacion_contacto': informacion_contacto, 
        'especies': especies_con_animales,
    }

    return render(request, 'index.html', context)

def animales(request):
    especies_con_animales = Especie.objects.filter(animal__isnull=False).distinct()
    especies_data = []
    animales = Animal.objects.filter(disponible=True)

    # Filtros
    nombre = request.POST.get('nombre') or request.GET.get('nombre')
    raza = request.POST.get('raza') or request.GET.get('raza')
    sexo = request.POST.get('sexo') or request.GET.get('sexo')
    tamano = request.POST.get('tamano') or request.GET.get('tamano')
    categoria_edad = request.POST.get('categoria_edad') or request.GET.get('categoria_edad')

    if nombre:
        animales = animales.filter(nombre__icontains=nombre)
    if raza:
        animales = animales.filter(raza=raza)
    if sexo:
        animales = animales.filter(sexo=sexo)
    if tamano:
        animales = animales.filter(tamano=tamano)
    if categoria_edad:
        animales = animales.filter(categoria_edad=categoria_edad)

    # Paginación por especie
    for especie in especies_con_animales:
        animales_especie = animales.filter(especie=especie)
        paginator = Paginator(animales_especie, 6)  # Puedes ajustar el número por página
        page_number = request.GET.get(f'page_{especie.id}') or 1
        page_obj = paginator.get_page(page_number)
        especies_data.append({'especie': especie, 'page_obj': page_obj})

    context = {
        'especies_data': especies_data,
        'especies': especies_con_animales,
        'razas': Animal.objects.values('raza').distinct()
    }

    return render(request, 'animales.html', context)