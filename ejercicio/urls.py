from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ultimoVoto/<int:id_pijama>',views.ultimoVoto, name='ultimoVoto'),
    path('pijamas/listarMalos/<int:id_cliente>',views.listarMalos,name="listarMalos"),
    path('clientes/listarSinVotos',views.listarSinVotos,name="listaSinVotos"),
    path('cuentasBancarias/CaixaUnicaja/<str:nombre>',views.listarCuentas,name="listaCuentas"),
    path('votos2023EnAdelante',views.votos5estrellas,name="votos5estrellas"),
    path('mediaMayor2,5',views.mediaMayor,name="mediaMayor"),
]