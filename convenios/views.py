from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,ListView,CreateView

# Create your views here.
from convenios.models import Convenio
from convenios.forms import CrearconvenioForms


class Inicio(TemplateView):
  template_name = 'Inicio/Index.html'
  page_title = 'Inicio'
      
  def get_context_data(self, **kwargs):
    context = super(Inicio, self).get_context_data(**kwargs)
    context["page_title"] = self.page_title
    return context
  

class InicioConvenio(ListView):
  model = Convenio
  template_name = 'convenios/index.html'
  page_title = 'Convenios'

  def get_context_data(self, **kwargs):
    context = super(InicioConvenio, self).get_context_data(**kwargs)  
    context['page_title'] = self.page_title
    return context
  
class CrearConvenio(CreateView):
  model = Convenio
  form_class = CrearconvenioForms
  success_url = 