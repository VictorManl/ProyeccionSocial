from django.contrib import admin
from django.forms import NullBooleanField
from convenios.models import Entidad, Nivel, Convenio

# Register your models here.


admin.site.register(Entidad)
admin.site.register(Nivel)
admin.site.register(Convenio)