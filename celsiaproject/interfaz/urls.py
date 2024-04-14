from django.urls import path
from .views import HomeCelsiaPageView, detallesCelsiaPageView, informeCelsiaPageView, anomaliasCelsiaPageView
from .views import HomeClientePageView, consumoClientePageView, estadisticasClientePageView, nosotrosClientePageView

urlpatterns = [

    ## urls vista celsia
    path('homeCelsia/', HomeCelsiaPageView.as_view(), name='home_celsia'),
    path('detalles/', detallesCelsiaPageView.as_view(), name='detalles_celsia'),
    path('informe/', informeCelsiaPageView.as_view(), name='informe_celsia'),
    path('anomalias/', anomaliasCelsiaPageView.as_view(), name='anomalias_celsia'),

    ## urls vista cliente
    path('homeCliente/', HomeClientePageView.as_view(), name='home_cliente'),
    path('consumo/', consumoClientePageView.as_view(), name='consumo_cliente'),
    path('estadisticasCliente/', estadisticasClientePageView.as_view(), name='estadisticas_cliente'),
    path('nosotros/', nosotrosClientePageView.as_view(), name='nosotros'),

]

                        