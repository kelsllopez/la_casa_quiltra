from django.db import models
from django.contrib.auth.models import User

class Galeria(models.Model):
    nombre = models.CharField(max_length=255, help_text="Ingresa el nombre de la imagen o galería.")
    descripcion = models.TextField(help_text="Descripción de la imagen (opcional).", null=True, blank=True)
    fecha = models.DateField(help_text="La fecha de la imagen .")

    creado_el = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación del especie.")
    actualizado_el = models.DateTimeField(auto_now=True, help_text="Fecha y hora de última modificación del especie.")
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='galeria_creado_por', help_text="Usuario que creó la galeria.")
    actualizado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='galeria_actualizado_por', help_text="Usuario que modificó la galeria.")

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Obtener el request si se pasa desde la vista
        if not self.pk and request:  # Si el evento es nuevo
            self.creado_por = request.user
        if request:  # Siempre actualizar el usuario que lo modifica
            self.actualizado_por = request.user
        super(Galeria, self).save(*args, **kwargs)
    def __str__(self):
        return self.nombre


class Imagen(models.Model):
    galeria = models.ForeignKey(Galeria, related_name='imagenes', on_delete=models.CASCADE, null=False, blank=False)
    imagen = models.ImageField(upload_to='galeria/', help_text="Sube la imagen para la galería.", null=False, blank=False)

    def __str__(self):
        return f"Imagen {self.id} de {self.galeria.nombre}"
