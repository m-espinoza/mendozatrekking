from .models import *
from django.views import generic
from django.urls import reverse
from django.http import HttpResponse
from django.template import loader


def index(request):
    lista_destinos =  Destino.objects.all().order_by('posicion')
    template = loader.get_template("index.html")
    context = {
        "lista_destinos": lista_destinos,
    }
    return HttpResponse(template.render(context, request))