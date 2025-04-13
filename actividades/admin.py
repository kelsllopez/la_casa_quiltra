from django.utils.safestring import mark_safe
from django.contrib import admin
from .models import Evento, Charla, Taller, Conversatorio, JornadaAdopcion

# Función personalizada para mostrar la imagen en el admin
def imagen_thumbnail(obj):
    if obj.imagen:
        return mark_safe(f'<img src="{obj.imagen.url}" width="100" height="100" />')
    return "No imagen"

# Registro de modelos con la personalización de la imagen
@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha', 'hora', 'lugar', 'organizador', 'imagen_thumbnail', 'creado_el', 'actualizado_el', 'creado_por', 'actualizado_por')
    exclude = ('creado_por', 'actualizado_por') 
    search_fields = ('titulo', 'organizador')
    list_filter = ('fecha', 'lugar')

    # Configurar la columna 'imagen' para usar la función personalizada
    def imagen_thumbnail(self, obj):
        if obj.imagen:
            return mark_safe(f'<img src="{obj.imagen.url}" width="100" height="100" />')
        return "No imagen"
    imagen_thumbnail.short_description = 'Imagen'

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Si el objeto es nuevo
            obj.creado_por = request.user
        obj.actualizado_por = request.user  # Siempre actualizar el usuario que modifica
        super().save_model(request, obj, form, change)

@admin.register(Charla)
class CharlaAdmin(admin.ModelAdmin):
    list_display = ('tema', 'fecha', 'hora', 'ubicacion', 'quien_dara_la_charla', 'imagen_thumbnail', 'creado_el', 'actualizado_el', 'creado_por', 'actualizado_por')
    exclude = ('creado_por', 'actualizado_por') 
    search_fields = ('tema', 'quien_dara_la_charla')
    list_filter = ('fecha', 'ubicacion', 'modalidad')

    def imagen_thumbnail(self, obj):
        if obj.imagen:
            return mark_safe(f'<img src="{obj.imagen.url}" width="100" height="100" />')
        return "No imagen"
    imagen_thumbnail.short_description = 'Imagen'

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Si la charla es nueva
            obj.creado_por = request.user
        obj.actualizado_por = request.user  # Siempre actualizar el usuario que la modifica
        super().save_model(request, obj, form, change)

@admin.register(Taller)
class TallerAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'hora', 'lugar', 'imagen_thumbnail', 'creado_el', 'actualizado_el', 'creado_por', 'actualizado_por')
    exclude = ('creado_por', 'actualizado_por')     
    search_fields = ('nombre',)
    list_filter = ('fecha', 'lugar')

    def imagen_thumbnail(self, obj):
        if obj.imagen:
            return mark_safe(f'<img src="{obj.imagen.url}" width="100" height="100" />')
        return "No imagen"
    imagen_thumbnail.short_description = 'Imagen'

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Si la charla es nueva
            obj.creado_por = request.user
        obj.actualizado_por = request.user  # Siempre actualizar el usuario que la modifica
        super().save_model(request, obj, form, change)

@admin.register(Conversatorio)
class ConversatorioAdmin(admin.ModelAdmin):
    list_display = ('tema', 'fecha', 'hora', 'ubicacion', 'moderador', 'imagen_thumbnail', 'creado_el', 'actualizado_el', 'creado_por', 'actualizado_por')
    exclude = ('creado_por', 'actualizado_por')         
    search_fields = ('tema', 'moderador')
    list_filter = ('fecha', 'ubicacion')

    def imagen_thumbnail(self, obj):
        if obj.imagen:
            return mark_safe(f'<img src="{obj.imagen.url}" width="100" height="100" />')
        return "No imagen"
    imagen_thumbnail.short_description = 'Imagen'

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Si la charla es nueva
            obj.creado_por = request.user
        obj.actualizado_por = request.user  # Siempre actualizar el usuario que la modifica
        super().save_model(request, obj, form, change)

@admin.register(JornadaAdopcion)
class JornadaAdopcionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'tipo_evento', 'imagen_thumbnail', 'creado_el', 'actualizado_el', 'creado_por', 'actualizado_por')
    exclude = ('creado_por', 'actualizado_por')             
    search_fields = ('nombre', 'tipo_evento')
    list_filter = ('fecha', 'tipo_evento')

    def imagen_thumbnail(self, obj):
        if obj.imagen:
            return mark_safe(f'<img src="{obj.imagen.url}" width="100" height="100" />')
        return "No imagen"
    imagen_thumbnail.short_description = 'Imagen'

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Si la charla es nueva
            obj.creado_por = request.user
        obj.actualizado_por = request.user  # Siempre actualizar el usuario que la modifica
        super().save_model(request, obj, form, change)