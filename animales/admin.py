from django.contrib import admin
from .models import *
from django.utils.html import mark_safe

class ImagenInline(admin.TabularInline):
    model = Imagen
    extra = 1  # Número de formularios adicionales vacíos
    fields = ('imagen',)  # Coloca los campos dentro de una tupla (coma al final)


@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'creado_el', 'actualizado_el', 'creado_por', 'actualizado_por')
    exclude = ('creado_por', 'actualizado_por') 
    search_fields = ('nombre',)

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Si el objeto es nuevo
            obj.creado_por = request.user
        obj.actualizado_por = request.user  # Siempre actualizar el usuario que modifica
        super().save_model(request, obj, form, change)



@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'sexo', 'tamano', 'estado', 'fecha_ingreso', 'disponible', 'creado_el', 'actualizado_el', 'creado_por', 'actualizado_por')
    exclude = ('creado_por', 'actualizado_por') 
    list_filter = ('especie', 'sexo', 'tamano', 'estado', 'disponible')
    search_fields = ('nombre', 'raza', 'ubicacion',)
    ordering = ('fecha_ingreso',)
    inlines = [ImagenInline]  # Añadimos las imágenes como un Inline en la galería


    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Si el objeto es nuevo
            obj.creado_por = request.user
        obj.actualizado_por = request.user  # Siempre actualizar el usuario que modifica
        super().save_model(request, obj, form, change)