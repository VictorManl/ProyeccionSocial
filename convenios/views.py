from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

# Create your views here.
from convenios.models import Convenio, Unidadejecutora, Nivel
from convenios.forms import CrearconvenioForm


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
    template_name = 'convenios/CrearConvenio.html'
    form_class = CrearconvenioForm
    success_url = reverse_lazy('InicioConvenios')
    page_title = 'Crear convenio'

    def get_context_data(self, **kwargs):
        context = super(CrearConvenio, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['form'] = self.form_class
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Guardado correctamente')
            return  HttpResponseRedirect(reverse_lazy('InicioConvenios'))
        else:
            messages.error(request, 'Oop ah ocurrido un error, por favor intentalo nuevamente')
            return HttpResponseRedirect(reverse_lazy('InicioConvenios'))
