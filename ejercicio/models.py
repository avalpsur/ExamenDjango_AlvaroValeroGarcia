from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models her

class Pijama(models.Model):
    modelo = models.CharField(max_length=50)
    talla = models.CharField(max_length=3)
    material = models.CharField(max_length=50)
    
    
class Cliente(models.Model):
    DNI = models.CharField(max_length=9,unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=100)
    edad = models.IntegerField()
    votacion = models.ManyToManyField(Pijama,through='Votaciones',related_name="votaciones_pijamas")
    
    
class CuentaBancaria(models.Model):
    ENTIDAD = [
        ("CA","Caixa"),
        ("BB","BBVA"),
        ("UN","Unicaja"),
        ("IN","ING"),
    ]
    
    numero = models.CharField(max_length=12,unique=True)
    entidad = models.CharField(
        max_length=2,
        choices=ENTIDAD,
        default='CA',
    )
    dinero = models.IntegerField()
    cliente = models.OneToOneField(Cliente,on_delete=models.CASCADE,related_name="cuentas_cliente")
    
class Votaciones(models.Model):
    PUNTUACION = [
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
    ]
    
    pijama = models.ForeignKey(Pijama,on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    
    puntuacion = models.IntegerField(
        choices=PUNTUACION,
        default='3',
    )
    
    comentario = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)
