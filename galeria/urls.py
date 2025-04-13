from django.urls import path
from . import views

urlpatterns = [

    path('', views.uwu, name='galeria'),  # Esta es la URL para la vista de actividades

]
