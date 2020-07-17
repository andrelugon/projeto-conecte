from django.urls import path, include
from .views import home_supermercadoficticio


urlpatterns = [
    path('', home_supermercadoficticio),

]