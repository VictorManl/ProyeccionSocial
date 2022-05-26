from django.urls import path
from convenios.views import InicioConvenio,Inicio, CrearConvenio


urlpatterns = [
  path('', Inicio.as_view(), name="Inicio"),
  path('Convenios', InicioConvenio.as_view(), name = 'InicioConvenios'),
  path('Convenios/Crear_convenio', CrearConvenio.as_view(), name = 'Crearconvenio'),
]