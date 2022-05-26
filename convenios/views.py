from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class Inicio(TemplateView):
  template_name = 'Base/Base.html'
  page_title = 'Base'

  def get_context_data(self, **kwargs):
    context = super(Inicio, self).get_context_data(**kwargs)
    context['page_title'] = self.page_title
    return context