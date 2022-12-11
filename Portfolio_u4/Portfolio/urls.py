from django.urls import path
from .views import mostrariniciosesion, listarportafolio, crearportafolio, mostrarregistro,LogoutView
"""from .views import LogoutView, mostrarbienvenida"""
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [

   
    path('', views.ip, name='mostrarpresentacion'),
    path('listarportafolio/', listarportafolio.as_view(), name='listarportafolio'),
    path('mostrariniciosesion/', mostrariniciosesion.as_view(), name='mostrariniciosesion'), 
    path('crearportafolio/', login_required(crearportafolio.as_view()), name='crearportafolio'), 
    path('mostrarregistro/', mostrarregistro.as_view(), name='mostrarregistro'),
    path('cerrarsesion/', LogoutView.as_view(), name='cerrarsesion'),

    
]
