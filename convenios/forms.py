from django import forms

from convenios.models import Convenio

class CrearconvenioForm(forms.ModelForm):
    class Meta:
        model = Convenio
        fields = [
            'conv_numero',
            'conv_organizacion',
            'conv_email',
            'conv_objeto',
            'conv_telefono',
            'conv_supervisor',
        ]
        labels = {
            'conv_numero':'Numero del convenio',
            'conv_organizacion':'Organizacion u empresa',
            'conv_email':'Email',
            'conv_objeto':'Objeto',
            'conv_telefono':'Telefono',
            'conv_supervisor':'Supervisor',
        }
