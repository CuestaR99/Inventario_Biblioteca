from rest_framework import routers
from .api import ProjectsViewset

#Funcion que crea el CRUD
router = routers.DefaultRouter()

#Para registrar las rutas basado en el conjunto de datos de la api
router.register('api/projects', ProjectsViewset, 'projects')

#Genera las URLS
urlpatterns = router.urls