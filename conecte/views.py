from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import cliente
from .forms import clienteForm

def home_conecte(request):
    return render(request, 'home.html')

def empresas(request):
    return render(request, 'empresas.html')

@login_required()
def controle(request):
    clientes = cliente.objects.all()
    return render(request, 'controle.html', {'cliente': clientes})

def cadastro(request):
    return render(request, 'cadastro.html')

def novo_cliente(request):
    form = clienteForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('controle')
    return render(request, 'cliente_form.html', {'form': form} )

def update_cliente(request, id):
    clientes = get_object_or_404(cliente, pk=id)
    form = clienteForm(request.POST or None, request.FILES or None, instance=clientes)

    if form.is_valid():
        form.save()
        return redirect('controle')

    return render(request, 'cliente_form.html', {'form': form})

def delete_cliente(request, id):
    clientes = get_object_or_404(cliente, pk=id)
    form = clienteForm(request.POST or None, request.FILES or None, instance=clientes)

    if request.method == 'POST':
        clientes.delete()
        return redirect('controle')

    return render(request, 'cliente_delete_confirm.html', {'form': form})

def buscar(request):
    list= cliente.objects.all()
    busca = request.GET.get('search')
    if busca:
        busca == 'search'
        if busca:
            list = cliente.objects.filter(atividade__icontains=busca) or \
                   cliente.objects.filter(nome_fantasia__icontains=busca ) or \
                   cliente.objects.filter(bairro__icontains=busca)

        return render(request, 'buscar.html', {'list': list})
    return render(request, 'buscar.html')

def espaço(value):
    return value.replace(' ', '')


