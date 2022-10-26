from django.shortcuts import render;
from hospedagem.models import Estadia;

# Create your views here.
def index(request):
    return render(request, 'index.html');

def listagem(request):
    lista = Estadia.objects.all();
    context = {'estadias' : lista};
    return render(request, 'listagem.html', context);

def detalhe(request, id_estadia):
    estadia = Estadia.objects.get(id = id_estadia);
    context = {'estadia' : estadia};
    return render(request, 'detalhe.html', context);