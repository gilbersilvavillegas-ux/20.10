"""
URL configuration for Gestcbo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import path
from .views import home, index, exit, Entrenador, reg_entrenador, atletas, editar_atleta, eliminar_atleta, reg_atleta, mensualidad, reg_mensualidades, horarios, rendi_atleta, registro_pruebas, editar_entrenador, eliminar_entrenador, categorias, registros_categorias, editar_categorias, eliminar_categoria

urlpatterns = [
    path('', home, name='home'),
    path("index/", index, name="index"),
    path("index/entrenador/", Entrenador, name="entrenador"),
    path("index/reg_entrenador/", reg_entrenador, name="reg_entrenador"),
    
    path('entrenadores/editar_entrenador/<str:ci_entrenador>/',editar_entrenador, name='editar_entrenador'),
    path('entrenadores/eliminar_entrenador/<str:ci_entrenador>/',eliminar_entrenador, name='eliminar_entrenador'),
    
    path("index/atletas/", atletas, name="atletas"),
    path("index/reg_atleta/", reg_atleta, name="reg_atleta"),
    path('atletas/editar_atletas/<str:id_atleta>/',editar_atleta, name='editar_atleta'),
    path('atletas/eliminar_atletas/<str:id_atleta>/',eliminar_atleta, name='eliminar_atleta'),
    
    path("index/mensualidad/", mensualidad, name="mensualidad"),
    path("index/mensualidad/reg_mensualidad/",reg_mensualidades, name="reg_mensualidades"), 
    
    path("index/horarios/", horarios, name="horarios"),
    path("index/Rendimiento/", rendi_atleta, name="rendi_atleta"),
    path("logout/", exit, name="exit"),
    path("index/registro_pruebas/", registro_pruebas, name="registro_pruebas"),
    
    path("index/categorias/", categorias, name="categorias"),
    path("index/registros_categoria/", registros_categorias, name="registros_categoria"),
    path('categorias/editar_categorias/<str:id_categoria>/',editar_categorias, name='editar_categorias'),
    path('categorias/eliminar_categorias/<str:id_categoria>/',eliminar_categoria, name='eliminar_categorias'),
    from django.urls import path
from . import views
# ... otras urls ...
    path('mensualidad/registrar/', views.registrar_mensualidad, name='registrar_mensualidad'),
    # ...
]