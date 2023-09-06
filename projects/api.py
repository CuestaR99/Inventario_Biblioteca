from .models import Libros
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer
#En esta clase se genera los valores que se van a consultar
class ProjectsViewset(viewsets.ModelViewSet):
    #Conjunto de datos
    queryset = Libros.objects.all()
    #AllowAny cualquier cliente puede consultar la informacion
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer


