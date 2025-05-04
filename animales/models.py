from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# 📌 Modelo de Especies
class Especie(models.Model):
    nombre = models.CharField(max_length=50, unique=True, help_text="Nombre de la especie, por ejemplo: Perro, Gato, Conejo.")
    creado_el = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación del especie.")
    actualizado_el = models.DateTimeField(auto_now=True, help_text="Fecha y hora de última modificación del especie.")
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='especie_creado_por', help_text="Usuario que creó el especie.")
    actualizado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='especie_actualizado_por', help_text="Usuario que modificó el especie.")

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Obtener el request si se pasa desde la vista
        if not self.pk and request:  # Si el evento es nuevo
            self.creado_por = request.user
        if request:  # Siempre actualizar el usuario que lo modifica
            self.actualizado_por = request.user
        super(Especie, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre


# 📌 Modelo de Animales
class Animal(models.Model):
    SEXO_CHOICES = [('Macho', 'Macho'), ('Hembra', 'Hembra')]
    TAMANO_CHOICES = [('Pequeño', 'Pequeño'), ('Mediano', 'Mediano'), ('Grande', 'Grande')]
    ESTADO_CHOICES = [('En adopción', 'En adopción'), ('Adoptado', 'Adoptado'), ('En tratamiento', 'En tratamiento')]
    EDAD_CATEGORIA_CHOICES = [
        ('Cachorro (0-1 año)', 'Cachorro (0-1 año)'),
        ('Joven (1-3 años)', 'Joven (1-3 años)'),
        ('Adulto (3-8 años)', 'Adulto (3-8 años)'),
        ('Senior (8 años o más)', 'Senior (8 años o más)')
    ]
    nombre = models.CharField(max_length=100, help_text="Nombre del animal.")
    edad = models.IntegerField(help_text="Edad exacta en años del animal (si se conoce).", null=True, blank=True)
    categoria_edad = models.CharField(max_length=21, choices=EDAD_CATEGORIA_CHOICES, help_text="Categoría de edad del animal.")    
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE, help_text="Especie a la que pertenece el animal.")
    raza = models.CharField(max_length=100, help_text="Raza del animal si aplica.")
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES, help_text="Sexo del animal.")
    tamano = models.CharField(max_length=10, choices=TAMANO_CHOICES, help_text="Tamaño del animal.")
    descripcion = models.TextField(help_text="Descripción general del animal, incluyendo su personalidad y necesidades especiales.")
    ubicacion = models.CharField(max_length=100, help_text="Ubicación actual del animal, por ejemplo: refugio central.")
    disponible = models.BooleanField(default=True, help_text="Indica si el animal está disponible para adopción.")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='En adopción', help_text="Estado actual del animal en el refugio.")
    fecha_ingreso = models.DateField(auto_now_add=True, help_text="Fecha en la que el animal ingresó al refugio.")
    vacunado = models.BooleanField(default=False, help_text="Indica si el animal tiene sus vacunas al día.")
    esterilizado = models.BooleanField(default=False, help_text="Indica si el animal ha sido esterilizado/castrado.")
    estado_salud = models.TextField(help_text="Información sobre la salud del animal.")
    notas_adicionales = models.TextField(blank=True, null=True, help_text="Notas adicionales o comentarios sobre el animal.")

    creado_el = models.DateTimeField(auto_now_add=True, help_text="Fecha y hora de creación del especie.")
    actualizado_el = models.DateTimeField(auto_now=True, help_text="Fecha y hora de última modificación del especie.")
    creado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='animal_creado_por', help_text="Usuario que creó el especie.")
    actualizado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='animal_actualizado_por', help_text="Usuario que modificó el especie.")

    def save(self, *args, **kwargs):
        request = kwargs.pop('request', None)  # Obtener el request si se pasa desde la vista
        if not self.pk and request:  # Si el evento es nuevo
            self.creado_por = request.user
        if request:  # Siempre actualizar el usuario que lo modifica
            self.actualizado_por = request.user
        super(Animal, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} ({self.especie.nombre})"

class Imagen(models.Model):
    galeria = models.ForeignKey(Animal, related_name='imagenes', on_delete=models.CASCADE)  # Aquí usamos 'imagenes' como related_name
    imagen = CloudinaryField('image', help_text="Imagen del animal.")

    def __str__(self):
        return f"Imagen {self.id} de {self.galeria.nombre}"