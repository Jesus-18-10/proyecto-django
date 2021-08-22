from cursos.models import Cursos
from django.contrib import admin
# Register your models here.
from .models import Cursos
from .models import Solicita_informacion
from .models import ComentarioContacto

class  AdministrarModelo(admin.ModelAdmin):
    list_display = ('nombre','precio','asesor','duracion_horas','descuento','porcentaje_descuento')    #campos que se van a visualizar
    readonly_fields = ('created','updated') #Visualizar campos agregados automaticamente

    search_fields = ('nombre','descripcion')    #Barra de busqueda
    list_filter = ('asesor','precio')    #Barra lateral para filtros
    date_hierarchy = 'created'  #Buscar por fecha

    list_per_page=4 #Se muestran de dos en dos los registros
    list_display_links=('nombre','precio','asesor')#En los campos que tendran click
    list_editable=('descuento','porcentaje_descuento',)#Editar los campos desde la lista
admin.site.register(Cursos,AdministrarModelo)#Registramos la app cursos en el administrador, tambien los  campos que no son visibles


class  Administrar_Solicita_informacion(admin.ModelAdmin):
    list_display = ('id','usuario','mensaje','cursodeinteres')
    readonly_fields = ('id','created','updated')#Visualizar campos agregados automaticamente

    search_fields = ('id','usuario','mensaje')#Barra de busqueda
    list_filter = ('estudiante','calificacion','cursodeinteres')    #Barra lateral para filtros
    date_hierarchy = 'created' #Buscar por fecha

    list_display_links=('id','usuario','mensaje','cursodeinteres')#En los campos que tendran click
    list_per_page=4 #Se muestran de dos en dos los registros
    
    
admin.site.register(Solicita_informacion,Administrar_Solicita_informacion)



class  AdministrarComentarioContacto(admin.ModelAdmin):
    list_display = ('id','usuario','mensaje','imagen')
    readonly_fields = ('created','id')

    search_fields = ('id','usuario','mensaje')
    date_hierarchy = 'created'
    list_filter = ('usuario','mensaje')    #Barra lateral para filtros

    list_display_links=('id','usuario','mensaje','imagen')
    list_per_page=4 #Se muestran de dos en dos los registros
    
    
#admin.site.register(ComentarioContacto,AdministrarComentarioContacto)

