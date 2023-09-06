from rest_framework import serializers
#Importar los modelos del proyecto
from .models import Libros
#Para realizar las respectivas peticiones POST, PUT, GET, y DELETE.
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        #Nombre del modelo
        model = Libros
        #Campos a ser consultados
        fields = ('id', 'titulo', 'autor', 'ano_publicacion','mes_publicacion', 'dia_publicacion', 'genero')
        