from django.shortcuts import render
from django.db.models import Q,Avg
from .models import *

#Create your views here
def index(request):
    return render(request,'index.html')


#Último voto que se realizó en un modelo principal en concreto
def ultimoVoto(request,id_pijama):
    #No hago el prefetch_related de pijama porque solo me pide los datos del cliente
    voto = Votaciones.objects.prefetch_related("cliente")
    voto = voto.filter(pijama=id_pijama).order_by("-fecha")[0:1].get()
    return render(request,'votaciones/ultimoVoto.html',{"voto":voto})


#Todos los pijamas que tengan una valoración menor a 3 y que realizó un cliente en concreto
def listarMalos(request,id_cliente):
    pijamas = Pijama.objects.filter(
        #Según el enunciado, hay que filtrar las puntuaciones menores que 3, por lo que el 3 no se tiene en cuenta
        votaciones__puntuacion__lt=3,
        votaciones__cliente=id_cliente
    ).all()
    return render(request,'pijamas/lista.html',{"pijamas":pijamas})


#Todos los clientes que no han votado
def listarSinVotos(request):
    #No hago el prefetch_related para optimizar la query, puesto que el cliente nunca va a tener votaciones
    clientes = Cliente.objects.filter(votaciones=None).all()
    return render(request,'clientes/lista.html',{"clientes":clientes})


#Cuentas de la Caixa o Unicaja de un cliente en concreto según su nombre
def listarCuentas(request,nombre):
    cuentas = CuentaBancaria.objects.select_related("cliente").filter(
        Q(entidad="CA") | Q(entidad="UN"),
        cliente__nombre=nombre
    ).all()
    return render(request,'cuentas/lista.html',{"cuentas":cuentas})


def votos5estrellas(request):
    votos = Votaciones.objects.prefetch_related("cliente")
    #Todos los clientes tienen una cuenta bancaria asociada
    votos = votos.filter(fecha__year__gte=2023,puntuacion=5).all()
    return render(request,'votaciones/lista.html',{"votos":votos})


def mediaMayor(request):
    #Esta forma de calcular la media está en la documentación de Django. Lo hice igual en el otro trabajo
    media = Votaciones.objects.aggregate(puntuacion__avg=Avg("puntuacion"))
    #No me ha dado tiempo a terminar lo que pide el enunciado :'c
    pijamas = Pijama.objects.filter(votaciones__puntuacion__gt=2.5)
    return render(request,'pijamas/lista.html',{"pijamas":pijamas})


#Páginas de Error
def mi_error_400(request,exception=None):
    return render(request, 'errores/400.html',None,None,400)

def mi_error_403(request,exception=None):
    return render(request, 'errores/403.html',None,None,403)

def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html',None,None,404)

def mi_error_500(request,exception=None):
    return render(request, 'errores/500.html',None,None,500)