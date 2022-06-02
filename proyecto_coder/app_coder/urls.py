from django.urls import path
from . import views


urlpatterns = [
    path("" , views.inicio),
    path("cursos" , views.cursos),
    path("alta_curso/<nombre>" , views.alta_curso)
    

]
