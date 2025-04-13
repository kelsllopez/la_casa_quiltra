from django.contrib import admin
from django.utils.html import mark_safe
from .models import Galeria, Imagen

class ImagenInline(admin.TabularInline):
    model = Imagen
    extra = 1  # Número de formularios adicionales vacíos
    fields = ('imagen',)  # Coloca los campos dentro de una tupla (coma al final)

@admin.register(Galeria)
class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'mostrar_imagen', 'creado_el', 'actualizado_el', 'creado_por', 'actualizado_por')  # Muestra estos campos en la lista del admin
    exclude = ('creado_por', 'actualizado_por')     
    search_fields = ('nombre', 'descripcion')  # Permite buscar por nombre y descripción
    list_filter = ('fecha',)  # Agrega un filtro por fecha

    inlines = [ImagenInline]  # Añadimos las imágenes como un Inline en la galería

    fieldsets = (
        (None, {
            'fields': ('nombre', 'descripcion', 'fecha')
        }),
    )

    def mostrar_imagen(self, obj):
        # Muestra la imagen en el admin si existe
        if obj.imagenes.exists():  # Usar 'imagenes' en lugar de 'imagen_set'
            imagen = obj.imagenes.first()  # Obtiene la primera imagen asociada
            return mark_safe(f'<img src="{imagen.imagen.url}" width="100" />')
        return "No hay imagen"
    
    mostrar_imagen.short_description = 'Imagen de la galería'

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Si el objeto es nuevo
            obj.creado_por = request.user
        obj.actualizado_por = request.user  # Siempre actualizar el usuario que modifica
        super().save_model(request, obj, form, change)