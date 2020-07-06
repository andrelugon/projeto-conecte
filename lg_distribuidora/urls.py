from django.urls import path, include
from .views import home_lgdistribuidora


urlpatterns = [
    path('', home_lgdistribuidora),

]