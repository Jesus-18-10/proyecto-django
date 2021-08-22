"""CursosDjango URL Configuration

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
from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from Contenido import views
from cursos import views as views_cursos
from django.conf import settings

urlpatterns = [
    # path('jet/', include('jet.urls')),
    #path('jet /dashboard', include ('jet.dashboard.urls','jet-dashboard')),

    path('admin/', admin.site.urls),
    path('',views.principal, name="PaginaPrincipal"),
    path('cursos/',views_cursos.cursos, name="Cursos"),
    path('contacto/',views_cursos.contacto, name="Contacto"),
     path('Agregar curso/',views_cursos.addcurso, name="CursoNuevo"),

    path('opiniones/',views_cursos.opiniones, name="Opiniones"),
    path('registrar/',views_cursos.registrar, name="Registrar"),
    path('registrar_solicita/',views_cursos.registrar_solicita, name="Registrar_Solicita"),

    path('Registrar_Curso/',views_cursos.registrar_curso, name="Registrar_Curso"),

    path('eliminarComentario/<int:id>/', views_cursos.eliminarComentarioContacto, name='Eliminar'),

    path('eliminarcurso/<int:id>/', views_cursos.eliminarCurso, name='EliminarCurso'),

    path('editar/<int:id>/',views_cursos.ConsultaIndividual, name="Editar"),
    
    path('registrareditar/<int:id>/',views_cursos.editar_Curso, name="RegistrarEditar"),


    path('administrador/',views_cursos.administrador, name="Administrador"),

    path('registrate/',views_cursos.registrate, name="Registrate"),
    path('Registrar_usuario/',views_cursos.Registrar_usuario, name="Registrar_usuario"),
    
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
  
]



#Agregamos este codigo para que se puedan visualizar las imagenes
if settings.DEBUG:
     from django.conf.urls.static import static
     urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
