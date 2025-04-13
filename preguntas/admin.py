from django.contrib import admin
from .models import Pregunta

# Register your models here.

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('pregunta', 'respuesta', 'creado_el', 'actualizado_el', 'creado_por', 'actualizado_por')  # Muestra estos campos en la lista del admin
    exclude = ('creado_por', 'actualizado_por')     
    search_fields = ('pregunta',)
    list_filter = ('pregunta',)
    ordering = ('pregunta',)


    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Si el objeto es nuevo
            obj.creado_por = request.user
        obj.actualizado_por = request.user  # Siempre actualizar el usuario que modifica
        super().save_model(request, obj, form, change)
admin.site.register(Pregunta, PreguntaAdmin)
