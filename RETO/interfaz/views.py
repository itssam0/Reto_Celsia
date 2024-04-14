from django.shortcuts import render
from django.views.generic import TemplateView


## Vistas de la empresa
class HomeCelsiaPageView(TemplateView):
    template_name = 'vistaCelsia/homeCelsia.html'

class detallesCelsiaPageView(TemplateView):
    template_name = 'vistaCelsia/detalles.html'

class informeCelsiaPageView(TemplateView):
    template_name = 'vistaCelsia/informe.html'

class anomaliasCelsiaPageView(TemplateView):
    template_name = 'vistaCelsia/anomalias.html'


## Vistas del cliente
class HomeClientePageView(TemplateView):
    template_name = 'vistaCliente/homeCliente.html'

class consumoClientePageView(TemplateView):
    template_name = 'vistaCliente/consumo.html'

class estadisticasClientePageView(TemplateView):
    template_name = 'vistaCliente/estadisticas.html'

class nosotrosClientePageView(TemplateView):
    template_name = 'vistaCliente/nosotros.html'

