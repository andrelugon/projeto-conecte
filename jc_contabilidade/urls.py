from django.urls import path, include
from .views import home_jccontabilidade, produtos, servicos


urlpatterns = [
    path('', home_jccontabilidade),
    path('produtos', produtos),
    path('servicos', servicos),

]