from django.shortcuts import render
from django.http import HttpResponse
from . models import dado, produto, serviço

def home_supermercadoficticio(request):
    lista_dados = dado.objects.all()
    lista_produtos = produto.objects.all()
    lista_serviços = serviço.objects.all()

    data = {
            'dados_gerais': lista_dados,
            'anuncio_produtos': lista_produtos,
            'anuncio_serviços': lista_serviços,
    }

    return render(request, 'index.html', data)