from django.urls import path, include
from .views import home_supermercado_ficticio


urlpatterns = [
    path('', home_supermercado_ficticio),

]