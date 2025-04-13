from django.urls import path
from . import views

urlpatterns = [
    path('', views.nosotros, name='nosotros'),  
    path('contacto/', views.contacto, name='contacto'),

]
