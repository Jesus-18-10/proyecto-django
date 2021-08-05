"""prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django import urls
from django.urls.conf import include
from inicio import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from registros import views as views_registros

#Permite acceder a las variables de Media_URL y Media_ROOT que almacenan
urlpatterns = [
  #   path('jet/', include('jet.urls')),
   #  path('jet /dashboard', include ('jet.dashboard.urls','jet-dashboard')),
    path('admin/', admin.site.urls),
    path('',views_registros.registros, name="Principal"),
    #Indicamos que ahora la ruta principal  se encuentra en view registros
    path('contacto/',views_registros.contacto, name="Contacto"),
    path('formulario/',views.formulario, name="Formulario"),

    path('registrar/',views_registros.registrar, name="Registrar"),

    path('consultarComentario/',views_registros.consultarComentarioContacto, name="Comentarios"),

    path('eliminarComentario/<int:id>/', views_registros.eliminarComentarioContacto, name='Eliminar'),

    path('editar/<int:id>/',views_registros.ConsultaIndividual, name="Editar"),

    path('registrareditar/<int:id>/',views_registros.editar_ComentarioContacto, name="RegistrarEditar"),

    path('consulta1',views_registros.consulta, name="Consulta1"),

    path('consultasql',views_registros.consultasSQL, name="sql"),
    
    
    path('subir',views_registros.archivos, name="Subir"),


    path('seguridad',views_registros.seguridad, name="Seguridad"),
     
    path('seguridad1',views_registros.seguridad1, name="Seguridad2"),
    path('seguridad2',views_registros.seguridad2, name="Seguridad3"),

    path('seguridad3',views_registros.seguridad3, name="Seguridad4"),


   
]

#Agregamos este codigo para que se puedan visualizar las imagenes
if settings.DEBUG:
     from django.conf.urls.static import static
     urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

