from django.urls import path
from convenios.views import InicioConvenio,Inicio


urlpatterns = [
  
  path("", Inicio.as_view(), name="Inicio"),
  path('Convenios', InicioConvenio.as_view(), name = 'InicioConvenios'),
]