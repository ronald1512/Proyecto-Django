from django.db import models

#Una clase por cada tabla que se encuentre dentro del modelo de la base de datos

#Django crea automaticamente las llaves primarias auto-incrementables con el nombre de atributo 'id'
    
class Universidad( models.Model ):
    nombre = models.CharField( max_length = 75 )
    direccion = models.CharField( max_length = 250 ) 

class Facultad( models.Model ):
    nombre = models.CharField( max_length = 75 )
    universidad = models.ForeignKey(Universidad, on_delete = models.CASCADE) #definicion de una llave foranea







