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
    path('', home_conecte),
    path('empresas/', empresas),
    path('controle/', controle, name='controle' ),
    path('cadastro/', cadastro, name='cadastro' ),
    path('novo_cliente/', novo_cliente, name="novo_cliente"),
    path('update/<int:id>', update_cliente, name="update_cliente"),
    path('delete/<int:id>', delete_cliente, name="delete_cliente"),
    path('buscar/', buscar, name="buscar"),
]