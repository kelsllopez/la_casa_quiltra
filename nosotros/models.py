from django.db import models
from django.contrib.auth.models import User

class MiembroEquipo(models.Model):
    nombre = models.CharField(max_length=100,help_text="Ingresa el nombre completo del miembro del equipo")
    rol = models.CharField(max_length=100,help_text="Ingresa el rol del miembro dentro del equipo (Ej: Fundadora, Veterinario, etc.)")
    cargo = models.CharField(max_length=100,help_text="Especifica el cargo o puesto específico del miembro (Ej: Coordinadora, Voluntario, etc.)")
    imagen = models.ImageField(upload_to='miembros/',help_text="Sube la imagen para los Miembros.",blank=True,null=True)

    creado_el = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación del especie.")
    actualizado_el = models.DateTimeField(auto_now=True, help_text="Fecha y hora de última modificación del especie.")
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='equipo_creado_por')
    actualizado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='equipo_actualizado_por')

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Obtener el request si se pasa desde la vista
        if not self.pk and request:  # Si el evento es nuevo
            self.creado_por = request.user
        if request:  # Siempre actualizar el usuario que lo modifica
            self.actualizado_por = request.user
        super(MiembroEquipo, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} - {self.cargo}"


class SobreNosotros(models.Model):
    nombre_refugio = models.CharField(max_length=255, default="La casa de la Quiltra", help_text="Nombre del refugio")
    historia = models.TextField(help_text="Historia sobre la fundación del refugio",blank=True,null=True)
    mision = models.TextField(help_text="Misión del refugio",blank=True,null=True)
    vision = models.TextField(help_text="Visión del refugio",blank=True,null=True)
    fecha_fundacion = models.DateField(help_text="Fecha de fundación del refugio", default="2015-01-01",blank=True,null=True)
    animales_rescatados = models.PositiveIntegerField(default=1000, help_text="Número de animales rescatados y reubicados", null=True, blank=True)
    imagen = models.ImageField(upload_to='sobre_nosotros/', help_text="Imagen representativa del refugio.",blank=True,null=True)

    creado_el = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación del especie.")
    actualizado_el = models.DateTimeField(auto_now=True, help_text="Fecha y hora de última modificación del especie.")
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='nosotros_creado_por')
    actualizado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='nosotros_actualizado_por')

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Obtener el request si se pasa desde la vista
        if not self.pk and request:  # Si el evento es nuevo
            self.creado_por = request.user
        if request:  # Siempre actualizar el usuario que lo modifica
            self.actualizado_por = request.user
        super(SobreNosotros, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre_refugio} - {self.mision}"

    class Meta:
        verbose_name = "Sobre Nosotros"
        verbose_name_plural = "Sobre Nosotros"


class InformacionContacto(models.Model):
    # Información estática de contacto
    ubicacion = models.CharField(max_length=255, help_text="Dirección del refugio")
    telefono = models.CharField(max_length=15, help_text="Número de teléfono del refugio")
    email = models.EmailField(help_text="Correo electrónico de contacto")
    horario_lunes_sabado = models.CharField(max_length=50, help_text="Horario de lunes a sábado")
    horario_domingo = models.CharField(max_length=50, help_text="Horario de domingo")
    # Redes sociales
    facebook = models.URLField(max_length=255, help_text="Enlace a Facebook")
    instagram = models.URLField(max_length=255, help_text="Enlace a Instagram")
    tiktok = models.URLField(max_length=255, help_text="Enlace a TikTok")
    # Enlace de Esponsor
    esponsor_enlace = models.URLField(max_length=255, help_text="Enlace de Esponsor")

    creado_el = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación del especie.")
    actualizado_el = models.DateTimeField(auto_now=True, help_text="Fecha y hora de última modificación del especie.")
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='informacioncontacto_creado_por')
    actualizado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='informacioncontacto_actualizado_por')

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Obtener el request si se pasa desde la vista
        if not self.pk and request:  # Si el evento es nuevo
            self.creado_por = request.user
        if request:  # Siempre actualizar el usuario que lo modifica
            self.actualizado_por = request.user
        super(InformacionContacto, self).save(*args, **kwargs)

    def __str__(self):
        return f"Información de contacto - {self.ubicacion}"

    class Meta:
        verbose_name = "Información de Contacto"
        verbose_name_plural = "Información de Contacto"

class MensajeContacto(models.Model):
    # Campos para el formulario de contacto
    nombre_usuario = models.CharField(max_length=255, help_text="Nombre de la persona que contacta")
    email_usuario = models.EmailField(help_text="Correo electrónico de la persona que contacta")
    asunto = models.CharField(max_length=255, help_text="Asunto del mensaje")
    mensaje = models.TextField(help_text="Cuerpo del mensaje")
    fecha_envio = models.DateTimeField(auto_now_add=True, help_text="Fecha en que se envió el mensaje")

    creado_el = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación del especie.")
    actualizado_el = models.DateTimeField(auto_now=True, help_text="Fecha y hora de última modificación del especie.")
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='mensajedecontacto_creado_por')
    actualizado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='mensajedecontacto_actualizado_por')

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Obtener el request si se pasa desde la vista
        if not self.pk and request:  # Si el evento es nuevo
            self.creado_por = request.user
        if request:  # Siempre actualizar el usuario que lo modifica
            self.actualizado_por = request.user
        super(MensajeContacto, self).save(*args, **kwargs)

    def __str__(self):
        return f"Mensaje de {self.nombre_usuario} - Asunto: {self.asunto}"

    class Meta:
        verbose_name = "Mensaje de Contacto"
        verbose_name_plural = "Mensajes de Contacto"

class Voluntario(models.Model):
    nombre = models.CharField(max_length=100, help_text="Nombre del voluntario.")
    contacto = models.CharField(max_length=100, help_text="Teléfono o correo de contacto.")
    email = models.EmailField(help_text="Correo electrónico del voluntario.")
    fecha_registro = models.DateField(auto_now_add=True, help_text="Fecha en la que el voluntario se registró.")
    disponibilidad = models.CharField(max_length=50,
        choices=[
            ('Fines de semana', 'Fines de semana'), 
            ('Entre semana', 'Entre semana'), 
            ('Tiempo completo', 'Tiempo completo')
        ],
        help_text="Disponibilidad del voluntario.")
    habilidades = models.TextField(help_text="Habilidades o experiencia del voluntario.")
    imagen = models.ImageField(upload_to='voluntarios/', help_text="Imagen del voluntario.",blank=True,null=True)

    creado_el = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación del especie.")
    actualizado_el = models.DateTimeField(auto_now=True, help_text="Fecha y hora de última modificación del especie.")
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='voluntario_creado_por')
    actualizado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='voluntario_actualizado_por')

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Obtener el request si se pasa desde la vista
        if not self.pk and request:  # Si el evento es nuevo
            self.creado_por = request.user
        if request:  # Siempre actualizar el usuario que lo modifica
            self.actualizado_por = request.user
        super(Voluntario, self).save(*args, **kwargs)


    def __str__(self):
        return f"{self.nombre} - {self.disponibilidad}"
