from django.urls import path
from convenios.views import Inicio


urlpatterns = [
  path('', Inicio.as_view(), name = 'Inicio'),
]