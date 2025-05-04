from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

class Evento(models.Model):
    titulo = models.CharField(max_length=100, help_text="Título del evento.", null=False, blank=False)
    descripcion = models.TextField(help_text="Descripción del evento.", null=True, blank=True)
    fecha = models.DateField(help_text="Fecha en la que se realizará el evento.", null=False, blank=False)
    hora = models.TimeField(help_text="Hora en la que se realizará el evento.", null=False, blank=False) 
    lugar = models.CharField(max_length=200, help_text="Ubicación donde se llevará a cabo el evento.", null=False, blank=False)
    organizador = models.CharField(max_length=100, help_text="Nombre del organizador del evento.", null=True, blank=True)
    imagen = CloudinaryField('image', blank=False, null=False, help_text="Imagen del evento.")
    creado_el = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación del evento.")
    actualizado_el = models.DateTimeField(auto_now=True, help_text="Fecha y hora de última modificación del evento.")
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='evento_creado_por', help_text="Usuario que creó el evento.")
    actualizado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='evento_actualizado_por', help_text="Usuario que modificó el evento.")

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Obtener el request si se pasa desde la vista
        if not self.pk and request:  # Si el evento es nuevo
            self.creado_por = request.user
        if request:  # Siempre actualizar el usuario que lo modifica
            self.actualizado_por = request.user
        super(Evento, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.titulo} - {self.fecha} {self.hora if self.hora else ''}"


class Charla(models.Model):
    MODALIDAD_CHOICES = [
        ('presencial', 'Presencial'),
        ('virtual', 'Virtual'),
    ]
    tema = models.CharField(max_length=255, help_text="Tema principal de la charla.", null=False, blank=False)
    descripcion = models.TextField(help_text="Descripción detallada de la charla.", null=True, blank=True)
    fecha = models.DateField(help_text="Fecha en la que se realizará la charla.", null=False, blank=False)
    hora = models.TimeField(help_text="Hora de inicio de la charla.", null=False, blank=False)
    actividades = models.TextField(help_text="Descripción de las actividades que se realizarán en la charla.", null=True, blank=True)
    imagen = CloudinaryField('image', null=True, blank=True, help_text="Imagen opcional para la charla.")
    quien_dara_la_charla = models.CharField(max_length=255, help_text="Nombre de la persona que dará la charla.", null=False, blank=False)
    ubicacion = models.CharField(max_length=255, help_text="Ubicación de la charla.", null=False, blank=False)
    modalidad = models.CharField(
        max_length=10,
        choices=MODALIDAD_CHOICES,
        default='presencial',
        help_text="Modalidad de la charla (Presencial o Virtual)."
    )
    creado_el = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación de la charla.")
    actualizado_el = models.DateTimeField(auto_now=True, help_text="Fecha y hora de última modificación de la charla.")
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='charla_creado_por', help_text="Usuario que creó la charla.")
    actualizado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='charla_actualizado_por', help_text="Usuario que modificó la charla.")


    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Obtener el request si se pasa desde la vista
        if not self.pk and request:  # Si el evento es nuevo
            self.creado_por = request.user
        if request:  # Siempre actualizar el usuario que lo modifica
            self.actualizado_por = request.user
        super(Charla, self).save(*args, **kwargs)

    def __str__(self):
        return f"Charla sobre {self.tema} - {self.fecha} a las {self.hora} ({self.get_modalidad_display()}) por {self.quien_dara_la_charla} en {self.ubicacion}"

class Taller(models.Model):
    nombre = models.CharField(max_length=255, help_text="Nombre del taller.", null=False, blank=False)
    descripcion = models.TextField(help_text="Descripción detallada del taller.", null=True, blank=True)
    fecha = models.DateField(help_text="Fecha en la que se realizará el taller.", null=False, blank=False)
    hora = models.TimeField(help_text="Hora de inicio del taller.", null=False, blank=False)
    lugar = models.CharField(max_length=255, help_text="Lugar donde se realizará el taller.", null=False, blank=False)
    imagen = CloudinaryField('image', null=False, blank=False, help_text="Imagen opcional para el taller.")
    creado_el = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación del taller .")
    actualizado_el = models.DateTimeField(auto_now=True, help_text="Fecha y hora de última modificación del taller.")
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='taller_creado_por', help_text="Usuario que creó el taller.")
    actualizado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='taller_actualizado_por', help_text="Usuario que modificó el taller.")
    
    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Obtener el request si se pasa desde la vista
        if not self.pk and request:  # Si el evento es nuevo
            self.creado_por = request.user
        if request:  # Siempre actualizar el usuario que lo modifica
            self.actualizado_por = request.user
        super(Taller, self).save(*args, **kwargs)

    def __str__(self):
        return f"Taller: {self.nombre} - {self.fecha} a las {self.hora} en {self.lugar}"


class Conversatorio(models.Model):
    tema = models.CharField(max_length=255, help_text="Tema principal del conversatorio.", null=False, blank=False)
    descripcion = models.TextField(help_text="Descripción detallada del conversatorio.", null=True, blank=True)
    fecha = models.DateField(help_text="Fecha en la que se realizará el conversatorio.", null=False, blank=False)
    hora = models.TimeField(help_text="Hora de inicio del conversatorio.", null=False, blank=False)
    moderador = models.CharField(max_length=255, help_text="Nombre del moderador del conversatorio.", null=False, blank=False)
    ubicacion = models.CharField(max_length=255, help_text="Ubicación del conversatorio.", null=False, blank=False)
    imagen = CloudinaryField('image', null=False, blank=False, help_text="Imagen opcional para el conversatorio.")
    creado_el = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación del taller .")
    actualizado_el = models.DateTimeField(auto_now=True, help_text="Fecha y hora de última modificación del taller.")
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='conversatorio_creado_por', help_text="Usuario que creó el conversatorio.")
    actualizado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='conversatorio_actualizado_por', help_text="Usuario que modificó el conversatorio.")
    
    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Obtener el request si se pasa desde la vista
        if not self.pk and request:  # Si el evento es nuevo
            self.creado_por = request.user
        if request:  # Siempre actualizar el usuario que lo modifica
            self.actualizado_por = request.user
        super(Conversatorio, self).save(*args, **kwargs)

    def __str__(self):
        return f"Conversatorio sobre {self.tema} - {self.fecha} a las {self.hora} en {self.ubicacion}"

class JornadaAdopcion(models.Model):
    nombre = models.CharField(max_length=255, help_text="Nombre del evento de adopción.", null=False, blank=False)
    descripcion = models.TextField(help_text="Descripción detallada del evento de adopción.", null=True, blank=True)
    fecha = models.DateField(help_text="Fecha de inicio del evento.", null=False, blank=False)
    hora = models.TimeField(help_text="Hora de inicio del evento.", null=False, blank=False)  
    actividades = models.TextField(help_text="Descripción de las actividades realizadas durante la jornada.", null=True, blank=True)
    tipo_evento = models.CharField(
        max_length=255, 
        choices=[('Animales Fest', 'Animales Fest'),
                 ('Huella con Historia', 'Huella con Historia'),
                 ('Expo Amor', 'Expo Amor'),
                 ('Festivales', 'Festivales'),
                 ('Expo', 'Expo')], 
        help_text="Tipo de evento (Animales Fest, Expo, etc.).", null=False, blank=False
    )
    ubicacion = models.CharField(max_length=255, help_text="Ubicación del evento de adopción.", null=False, blank=False)
    imagen = CloudinaryField('image', null=False, blank=False, help_text="Imagen opcional para la jornada de adopción.")
    creado_el = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación del jornada .")
    actualizado_el = models.DateTimeField(auto_now=True, help_text="Fecha y hora de última modificación del jornada.")
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='jornada_creado_por', help_text="Usuario que creó el jornada.")
    actualizado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='jornada_actualizado_por', help_text="Usuario que modificó el jornada.")
    
    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Obtener el request si se pasa desde la vista
        if not self.pk and request:  # Si el evento es nuevo
            self.creado_por = request.user
        if request:  # Siempre actualizar el usuario que lo modifica
            self.actualizado_por = request.user
        super(JornadaAdopcion, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} - {self.tipo_evento} del {self.fecha} a las {self.hora} en {self.ubicacion}"
