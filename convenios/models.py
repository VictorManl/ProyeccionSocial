from django.db import models


# Create your models here.
UNIDAD_CHOICES = (
    ('Dependencia','Dependencia'),
    ('Facultad','Facultad'),
)


class Entidad(models.Model):
    enti_id = models.AutoField('id', primary_key=True)
    enti_nombre = models.CharField('Nombre', max_length=100, null=False, blank=False)
    
    class Meta:
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'
        
    def __str__(self):
        texto = '{0}'
        return texto.format(self.enti_nombre)
    
    
class Nivel(models.Model):
    nive_id = models.AutoField('id',primary_key=True)
    nive_nombre = models.CharField('Nombre', max_length=200)
    
    class Meta:
        verbose_name = 'Nivel'
        verbose_name_plural = 'Nivel'
        
    def __str__(self):
        texto = '{0}'
        return texto.format(self.nive_nombre) 

class Unidadejecutora(models.Model):
    unej_id = models.AutoField('Id', primary_key = True)
    unej_unidad = models.CharField('Unidad', max_length=100, null=False, blank = False)

    class Meta:
        verbose_name = 'Unidad ejecutora'
        verbose_name_plural = 'Unidad ejecutora'

    def __str__(self):
        texto = '{0}'
        return texto.format(self.unej_unidad)

class Convenio(models.Model):
    conv_id = models.AutoField('Id', primary_key=True)
    conv_numero = models.CharField('Numero del convenio', max_length=50, null = False, blank=False)
    conv_fecha = models.DateField('Fecha',auto_now=False, auto_now_add=False),
    conv_organizacion = models.CharField('Organizacion', max_length=200, null=False, blank=False)
    conv_objeto = models.TextField('objeto', max_length=800, null=False, blank=False)
    conv_supervisor = models.CharField('Supervisor', max_length=200, null=False, blank=False)
    conv_email = models.EmailField('Email', max_length=254, null= False, blank=False)
    conv_telefono = models.IntegerField('Telefono', null=False, blank=False, default=0)
    conv_ejecutora = models.CharField('Unidad ejecutora', choices=UNIDAD_CHOICES, max_length=100, null=False, blank=False, default='-------')
    
    class Meta:
        verbose_name = 'Convenio'
        verbose_name_plural = 'Convenios'

    def __str__(self):
        texto = '{0} - {1}'
        return texto.format(self.conv_numero, self.conv_organizacion)