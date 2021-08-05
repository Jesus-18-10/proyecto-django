from django.shortcuts import render
from .forms import ComentarioContactoform

from .models import Comentario #Importamos el comentario contacto
from .models import ComentarioContacto #Importamos el comentario contacto
from .models import Alumnos # accedemos  al modelo alumnos que contiene la estrutura de la tabla
from django.shortcuts import get_object_or_404
import datetime
from django.http import HttpResponse


#Carga de archivos
from .models import Archivos 
from .forms import FormArchivos
from django.contrib import messages
from django.http import HttpResponse

from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def seguridad1(request):
    #Esta página es segura para cargar en un marco en cualquier sitio.
    return render(request,"registros/seguridad1.html")

@xframe_options_deny
def seguridad2(request):
    #Esta pagina No mostrara  ningun marco
    return render(request,"registros/seguridad2.html")

@xframe_options_sameorigin
def seguridad3(request):
    #Muestra en un marco si es del mismo origen
    return render(request,"registros/seguridad3.html")


def registros(request):
    alumnos=Alumnos.objects.all()# Indicamos que retornamos todos los objetos que se encuentran en el modelo alumnos
    return render(request,"registros/principal.html",{'alumnos':alumnos})
# Indicamos en lugar donde se renderizara la vista
#Enviamos la lista de alumnos recuperada

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoform(request.POST)
        if form.is_valid():
            form.save()
            #Definimos que cuando guarde el comentario se vaya a la pagina donde consulta los comentarios contacto
            comentarios=ComentarioContacto.objects.all()# Indicamos que retornamos todos los objetos que se encuentran en el modelo alumnos
            return render(request,"registros/consultaContacto.html",{'comentarios':comentarios})
            #return render(request, 'registros/contacto.html')
    form = ComentarioContactoform()
    return render(request,'registros/contacto.html',{'form':form})


def contacto(request):
    return render(request,"registros/contacto.html")

def consultarComentarioContacto(request):
    comentarios=ComentarioContacto.objects.all()# Indicamos que retornamos todos los objetos que se encuentran en el modelo alumnos
    return render(request,"registros/consultaContacto.html",{'comentarios':comentarios})#Le enviamos el objeto a la página


def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    comentarios=ComentarioContacto.objects.all()
    if request.method=='POST':
        comentario.delete()
        return render(request,"registros/consultaContacto.html",{'comentarios':comentarios})
    return render(request, confirmacion, {'object':comentario})



def comentario_editar(request, id, edicion='registros/editar_comentario.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoform(instance=comentario)
    return render(request,edicion,{'form':form,'object':comentario})


def registrar_editar(request,id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoform(request.POST,instance=comentario)
    if form.is_valid():
        form.save()
        
            #Definimos que cuando guarde el comentario se vaya a la pagina donde consulta los comentarios contacto
    comentarios=ComentarioContacto.objects.all()# Indicamos que retornamos todos los objetos que se encuentran en el modelo alumnos
    return render(request,"registros/consultaContacto.html",{'comentarios':comentarios})



def ConsultaIndividual(request, id):
    comentario = ComentarioContacto.objects.get(id=id)
    #Get permite establecer  
    return render(request,'registros/editar_comentario.html',{'comentario':comentario})

def editar_ComentarioContacto(request,id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoform(request.POST, instance=comentario)
    if form.is_valid():
        form.save()
        comentarios=ComentarioContacto.objects.all()# Indicamos que retornamos todos los objetos que se encuentran en el modelo alumnos
        return render(request,"registros/consultaContacto.html",{'comentarios':comentarios})  
            #Definimos que cuando guarde el comentario se vaya a la pagina donde consulta los comentarios contacto
    return render(request,"registros/editar_comentario.html",{'comentario':comentario})


#Funcion filter
def consulta1(request):
    alumnos=Alumnos.objects.filter(carrera="Tic")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

#Dos cunsultas
def consulta2(request):
    alumnos=Alumnos.objects.filter(carrera="Tic").filter(turno='Matutino')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

#Consultamos solo los campos requeridos
def consulta3(request):
    alumnos=Alumnos.objects.all().only('matricula','nombre','carrera','turno','imagen')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

#Filtro por Letras
def consulta4(request):
    alumnos=Alumnos.objects.filter(turno__contains="Vesp")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

#Fultro  por nombre
def consulta5(request):
    alumnos=Alumnos.objects.filter(nombre__in=['Juan','Ana'])
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

#Filtro de rangos
def consulta6(request):
    fechainicio = datetime.date(2021, 7, 1)
    fechafin =datetime.date(2021 ,7 ,16)
    alumnos=Alumnos.objects.filter(created__range=(fechainicio, fechafin))
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consulta(request):
    alumnos=Alumnos.objects.filter(comentario__coment ="<p>No&nbsp;inscrito</p>")
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

#consultasSQL
def consultasSQL(request):
    alumnos=Alumnos.objects.raw('SELECT id,matricula,nombre,carrera,turno,imagen FROM registros_alumnos WHERE carrera="Tic" ORDER BY turno DESC' )
    return render(request,"registros/consultas.html",{'alumnos':alumnos})


def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render(request,"registros/archivos.html")  
        else:
            messages.error(request,"Error al procesar el Formulario")  
    else:
        return render(request,"registros/archivos.html",{'archivo':Archivos})


def seguridad(request, nombre=None):
    nombre = request.GET.get('nombre')
    return render(request,"registros/seguridad.html",{'nombre':nombre})