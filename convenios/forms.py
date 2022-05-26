from cProfile import label
from tkinter import Widget
from django import forms

from convenios.models import Convenio



class CrearconvenioForms(forms.ModelForm):
    class Meta:
        model = Convenio
        fields = [
            "conv_numero",
            "conv_fecha",
            "conv_organizacion",
            "conv_objeto",
            "conv_supervisor",
            "conv_email",
            "conv_telefono",
        ],
        labels = {
            "conv_numero":"Numero del convenio",
            "conv_fecha":"Fecha del convenio",
            "conv_organizacion":"Empresa u Organización",
            "conv_objeto":"Objeto",
            "conv_supervisor":"Supervisor del convenio",
            "conv_email":"Email",
            "conv_telefono":"Telefono o Celular",
        }
        Widget = {
            'conv_fecha' : forms.DateField(),
            "conv_numero": forms.TextInput(attrs={'placeholder': 'Numero del convenio'}) ,
            "conv_fecha":forms.TextInput(attrs={'placeholder': 'Fecha del convenio'}) ,
            "conv_organizacion":forms.TextInput(attrs={'placeholder': 'Empresa u organización'}) ,
            "conv_objeto":forms.TextInput(attrs={'placeholder': 'Objeto'}) ,
            "conv_supervisor":forms.TextInput(attrs={'placeholder': 'Nombre completo del supervisor'}) ,
            "conv_email":forms.TextInput(attrs={'placeholder': 'Correo electronico'}) ,
            "conv_telefono":forms.TextInput(attrs={'placeholder': 'Numero de telefono o celulars'}) ,
        }