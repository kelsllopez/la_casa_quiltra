from django.contrib import admin
from django.utils.html import mark_safe
from .models import *

class MiembroEquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rol', 'cargo', 'mostrar_imagen', 'creado_el', 'actualizado_el', 'creado_por', 'actualizado_por')
    exclude = ('creado_por', 'actualizado_por')         
    search_fields = ('nombre', 'rol', 'cargo')
    list_filter = ('rol',)

    def mostrar_imagen(self, obj):
        # Muestra la imagen en el admin si existe
        if obj.imagen:
            return mark_safe(f'<img src="{obj.imagen.url}" width="100" />')
        return "No hay imagen"
    
    mostrar_imagen.short_description = 'Imagen del miembro'

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Si el objeto es nuevo
            obj.creado_por = request.user
        obj.actualizado_por = request.user  # Siempre actualizar el usuario que modifica
        super().save_model(request, obj, form, change)

admin.site.register(MiembroEquipo, MiembroEquipoAdmin)

@admin.register(SobreNosotros)
class SobreNosotrosAdmin(admin.ModelAdmin):
    list_display = ('nombre_refugio', 'fecha_fundacion', 'animales_rescatados', 'creado_el', 'actualizado_el', 'creado_por', 'actualizado_por')
    exclude = ('creado_por', 'actualizado_por')     
    search_fields = ('nombre_refugio',)
    list_filter = ('fecha_fundacion',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Si el objeto es nuevo
            obj.creado_por = request.user
        obj.actualizado_por = request.user  # Siempre actualizar el usuario que modifica
        super().save_model(request, obj, form, change)

@admin.register(InformacionContacto)
class InformacionContactoAdmin(admin.ModelAdmin):
    list_display = ('ubicacion', 'telefono', 'email', 'horario_lunes_sabado', 'horario_domingo', 'creado_el', 'actualizado_el', 'creado_por', 'actualizado_por')
    exclude = ('creado_por', 'actualizado_por')   
    search_fields = ('ubicacion', 'telefono', 'email')

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Si el objeto es nuevo
            obj.creado_por = request.user
        obj.actualizado_por = request.user  # Siempre actualizar el usuario que modifica
        super().save_model(request, obj, form, change)

@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre_usuario', 'asunto', 'email_usuario', 'fecha_envio', 'creado_el', 'actualizado_el', 'creado_por', 'actualizado_por')
    exclude = ('creado_por', 'actualizado_por')   
    search_fields = ('nombre_usuario', 'asunto', 'email_usuario')
    list_filter = ('fecha_envio',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Si el objeto es nuevo
            obj.creado_por = request.user
        obj.actualizado_por = request.user  # Siempre actualizar el usuario que modifica
        super().save_model(request, obj, form, change)

@admin.register(Voluntario)
class VoluntarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'disponibilidad', 'fecha_registro', 'contacto', 'mostrar_imagen_voluntario', 'creado_el', 'actualizado_el', 'creado_por', 'actualizado_por')
    exclude = ('creado_por', 'actualizado_por') 
    list_filter = ('disponibilidad',)
    search_fields = ('nombre', 'email', 'contacto')

    def mostrar_imagen_voluntario(self, obj):
        # Muestra la imagen en el admin si existe
        if obj.imagen:
            return mark_safe(f'<img src="{obj.imagen.url}" width="100" />')
        return "No hay imagen"
    
    mostrar_imagen_voluntario.short_description = 'Imagen del voluntario'
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Si el objeto es nuevo
            obj.creado_por = request.user
        obj.actualizado_por = request.user  # Siempre actualizar el usuario que modifica
        super().save_model(request, obj, form, change)