from django.urls import path
from . import views

urlpatterns = [

    path('actividades/', views.actividades, name='actividades'),  # Esta es la URL para la vista de actividades

]
