from django.urls import path, include
from .views import home_jccontabilidade


urlpatterns = [
    path('', home_jccontabilidade),

]