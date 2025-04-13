from .models import *
from actividades.models import *
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator

def nosotros(request):
    sobre_nosotros = SobreNosotros.objects.first()
    miembros = MiembroEquipo.objects.all()
    voluntarios = Voluntario.objects.all()
    # Obtiene las disponibilidades únicas de los voluntarios registrados
    disponibilidades = list(Voluntario.objects.values_list('disponibilidad', flat=True).distinct())
    context = {
        'sobre_nosotros': sobre_nosotros,
        'miembros': miembros,
        'voluntarios': voluntarios,
        "disponibilidades": disponibilidades,

    }

    return render(request, 'nosotros.html', context)

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

def contacto(request):
    informacion_contacto = InformacionContacto.objects.first()

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

            # Mostrar mensaje de éxito y redirigir inmediatamente
            messages.success(request, "Tu mensaje ha sido enviado con éxito.")
            return redirect("contacto")
        else:
            messages.error(request, "Todos los campos son obligatorios.")

    return render(request, "contacto.html", {
        'informacion_contacto': informacion_contacto,
    })