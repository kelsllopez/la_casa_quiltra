from django.db import models
from django.contrib.auth.models import User

class Pregunta(models.Model):
    pregunta = models.CharField(max_length=255,help_text="Ingresa la pregunta que quieres hacer (por ejemplo, '¿Cómo puedo registrarme?').") 
    respuesta = models.TextField(help_text="Escribe la respuesta a la pregunta (puede ser detallada).") 

    creado_el = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación del especie.")
    actualizado_el = models.DateTimeField(auto_now=True, help_text="Fecha y hora de última modificación del especie.")
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='preguntas_creado_por')
    actualizado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='preguntas_actualizado_por')

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Obtener el request si se pasa desde la vista
        if not self.pk and request:  # Si el evento es nuevo
            self.creado_por = request.user
        if request:  # Siempre actualizar el usuario que lo modifica
            self.actualizado_por = request.user
        super(Pregunta, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.pregunta

