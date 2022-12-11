from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib messages

# Create your views here.



class PortafolioP(TemplateView):
    template_name="index.html"
    