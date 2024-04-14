from django.urls import path
from .views import HomeCelsiaPageView, detallesCelsiaPageView, informeCelsiaPageView, anomaliasCelsiaPageView
from .views import HomeClientePageView, consumoClientePageView, estadisticasClientePageView, nosotrosClientePageView

urlpatterns = [

    ## urls vista celsia
    path('homeCelsia/', HomeCelsiaPageView.as_view(), name='homeCelsia'),
    path('detalles/', detallesCelsiaPageView.as_view(), name='detalles'),
    path('informe/', informeCelsiaPageView.as_view(), name='informe'),
    path('anomalias/', anomaliasCelsiaPageView.as_view(), name='anomalias'),

    ## urls vista cliente
    path('homeCliente/', HomeClientePageView.as_view(), name='homeCliente'),
    path('consumo/', consumoClientePageView.as_view(), name='consumo'),
    path('estadisticasCliente/', estadisticasClientePageView.as_view(), name='estadisticasCliente'),
    path('nosotros/', nosotrosClientePageView.as_view(), name='nosotros'),

]

                        