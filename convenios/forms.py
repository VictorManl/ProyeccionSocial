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
            'conv_ejecutora',
        ]
        labels = {
            'conv_numero':'Numero del convenio *',
            'conv_organizacion':'Organización o empresa *',
            'conv_email':'Correo electronico *',
            'conv_objeto':'Objeto del convenio *',
            'conv_telefono':'Telefono o celular *',
            'conv_supervisor':'Nombre completo del supervisor *',
            'conv_ejecutora':'Unidad ejecutora *',
        }
