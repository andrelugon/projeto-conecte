from django.urls import path, include
from .views import home_lgdistribuidora, produtos, servicos


urlpatterns = [
    path('', home_lgdistribuidora),
    path('produtos', produtos),
    path('servicos', servicos),

]