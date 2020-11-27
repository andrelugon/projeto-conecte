from django.shortcuts import render
from django.http import HttpResponse
from . models import dado, produto, serviço

def home_jccontabilidade(request):
    lista_dados = dado.objects.all()
    lista_produtos = produto.objects.all()
    lista_serviços = serviço.objects.all()

    data = {
            'dados_gerais': lista_dados,
            'anuncio_produtos': lista_produtos,
            'anuncio_serviços': lista_serviços,
    }

    return render(request, 'index_jccontabilidade.html', data)

def produtos(request):
    lista_dados = dado.objects.all()
    lista_produtos = produto.objects.all()
    lista_serviços = serviço.objects.all()

    data = {
            'dados_gerais': lista_dados,
            'anuncio_produtos': lista_produtos,
            'anuncio_serviços': lista_serviços,
    }

    return render(request, 'produtos.html', data)

def servicos(request):
    lista_dados = dado.objects.all()
    lista_produtos = produto.objects.all()
    lista_serviços = serviço.objects.all()

    data = {
            'dados_gerais': lista_dados,
            'anuncio_produtos': lista_produtos,
            'anuncio_serviços': lista_serviços,
    }

    return render(request, 'servicos.html', data)