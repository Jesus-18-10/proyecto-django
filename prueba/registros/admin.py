from registros.models import Alumnos

from django.contrib import admin
from .models import Alumnos
from .models import Comentario
from .models import ComentarioContacto
from .models import Archivos

# Register your models here.
class  AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display = ('matricula','nombre','carrera','turno','created')
    #campos que se van a visualizar
    search_fields = ('matricula','nombre','carrera','turno')
    #Barra de busqueda
    date_hierarchy = 'created'
    #Filtro por fecha de cracion
    list_filter = ('carrera','turno')
    #Barra lateral para filtros
    def get_readonly_fields(self, request,obj=None):
        if request.user.groups.filter(name="Usuarios").exists():
            #return ('created','updated','matricula','carrera','turno')
            return ('matricula','carrera','turno')
        else:
            return ('created','updated')
    list_per_page=2 #Se muestran de dos en dos los registros
    list_display_links=('matricula','carrera','nombre')#En los campos que tendran click
    list_editable=('turno',)#Editar los campos desde la lista

admin.site.register(Alumnos,AdministrarModelo)

class  AdministrarComentario(admin.ModelAdmin):
    list_display = ('id','coment')
    #campos que se van a visualizar
    search_fields = ('id','coment')
    #Barra de busqueda
    date_hierarchy = 'created'
    #Filtro por fecha de cracion
    readonly_fields = ('created','id')
admin.site.register(Comentario,AdministrarComentario)

class  AdministrarComentarioContacto(admin.ModelAdmin):
    list_display = ('id','usuario','mensaje')
    search_fields = ('id','usuario','mensaje')
    date_hierarchy = 'created'
    readonly_fields = ('created','id')
admin.site.register(ComentarioContacto,AdministrarComentarioContacto)

admin.site.register(Archivos)