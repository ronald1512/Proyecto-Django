from django.db import models

# Una clase por cada tabla que se encuentre dentro de la base de datos

class Cliente( models.Model ):
    nombre = models.CharField( max_length = 30 )
    direccion = models.CharField( max_length = 50 ) 
    email = models.EmailField() 
    telefono = models.IntegerField()

class Producto ( models.Model ):
    nombre = models.CharField( max_length = 30 )
    precio = models.IntegerField()

class Pedido( models.Model ):
    numero = models.IntegerField()
    fecha = models.DateField()



