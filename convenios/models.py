from cgitb import text
from re import S, T
from statistics import mode
from django.db import models
from django.forms import DateField

# Create your models here.

class Entidad(models.Model):
    enti_id = models.AutoField('id', primary_key=True)
    enti_nombre = models.CharField('Nombre', max_length=100, null=False, blank=False)
    
    class Meta:
        managed = True
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'
        
    def __str__(self):
        texto = '{0}'
        return texto.format(self.enti_nombre)
    
    
class Nivel(models.Model):
    nive_id = models.AutoField('id',primary_key=True)
    nive_nombre = models.CharField('Nombre', max_length=200)
    
    class Meta:
        managed = True
        verbose_name = 'Nivel'
        verbose_name_plural = 'Nivel'
        
    def __str__(self):
        texto = '{0}'
        return texto.format(self.nive_nombre) 
    
    
class Convenio(models.Model):
    conv_id = models.AutoField('Id', primary_key=True)
    conv_numero = models.CharField('Numero del convenio', max_length=50, null = False, blank=False)
    conv_fecha = models.DateField(),
    conv_organizacion = models.CharField('Organizacion', max_length=200, null=False, blank=False)
    conv_objeto = models.TextField('objeto', max_length=800, null=False, blank=False)
    conv_supervisor = models.CharField('Supervisor', max_length=200, null=False, blank=False)
    conv_email = models.EmailField('Email', max_length=254, null= False, blank=False)
    conv_telefono = models.IntegerField('Telefono', null=False, blank=False, default=0)
    
    class Meta:
        managed = True
        verbose_name = 'Convenio'
        verbose_name_plural = 'Convenios'

    def __str__(self):
        texto = '{0} - {1} - {2}'
        return texto.format(self.conv_numero, self.conv_fecha, self.conv_organizacion)