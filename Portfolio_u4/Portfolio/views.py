from django.views.generic import CreateView, TemplateView, ListView,UpdateView,DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from .models import portafolio
from .forms import portafolioforms, registrofroms
"""from django.contrib messages"""

from django.shortcuts import render
from ipware import get_client_ip
import sqlite3




# Create your views here.


class PortafolioP(TemplateView):
    template_name = "index.html"


class PortafolioD(TemplateView):
    template_name = "portfolio-details.html"

# Create your views here.

def ip(request):
    if request.method=="GET":
        client_ip, is_routable = get_client_ip(request)
        conexion = sqlite3.connect('db.sqlite3')
        conexion.execute("insert into Portfolio_ips(ip,enrutable) values (?,?)", (f"{client_ip}", f"{is_routable}"))
        conexion.commit()
        conexion.close()
    return render(request, 'index.html')



class mostrariniciosesion(LoginView):
    template_name = ('iniciosesion.html')
    success_url='/index'


class listarportafolio(ListView):
    model = portafolio
    template_name = ('listarportafolio.html')
    paginate_by=2
    def get_queryset(self, *args, **kwargs):
        lista = portafolio.objects.filter(autor=self.request.user)
        return lista


class crearportafolio(CreateView):
    model = portafolio
    form_class = portafolioforms
    template_name = ('crearportafolio.html')
    success_url = '/listarportafolio/'
    
    
class mostrarregistro(CreateView):
    form_class = registrofroms
    template_name = ('registrousuario.html')
    success_url = '/'
