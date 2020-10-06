from django.urls import path, include
from .views import (home_conecte,
                    empresas,
                    controle,
                    novo_cliente,
                    update_cliente,
                    delete_cliente,
                    cadastro,
                    buscar,
                    )



urlpatterns = [
    #path('', home_conecte),
    path('', buscar, name="buscar"),
    path('home/empresas/', empresas),
    path('home/controle/', controle, name='controle' ),
    path('home/cadastro/', cadastro, name='cadastro' ),
    path('home/novo_cliente/', novo_cliente, name="novo_cliente"),
    path('home/update/<int:id>', update_cliente, name="update_cliente"),
    path('home/delete/<int:id>', delete_cliente, name="delete_cliente"),

]