from django.shortcuts import render,HttpResponse
from .forms import ComentarioContactoform
from .forms import Solicita_informacionform
from .forms import Cursoform
from .models import Cursos # accedemos  al modelo Cursos que contiene la estrutura de la tabla
from .models import ComentarioContacto
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User

def cursos(request):
    cursos=Cursos.objects.all()# Indicamos que retornamos todos los objetos que se encuentran en el modelo alumnos
    return render(request,"cursos/cursos.html",{'cursos':cursos})


def registrar_solicita(request):
    cursos=Cursos.objects.all()
    if request.method == 'POST':
        form = Solicita_informacionform(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'cursos/contacto.html',{'cursos':cursos})
    form = Solicita_informacionform()
    return render(request,'cursos/contacto.html',{'cursos':cursos})
    #return render(request,'cursos/contacto.html',{'form':form})

def contacto(request):
    cursos=Cursos.objects.all()# Indicamos que retornamos todos los objetos que se encuentran en el modelo alumnos
    return render(request,"cursos/contacto.html",{'cursos':cursos})


def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            comentarios=ComentarioContacto.objects.all()# Indicamos que retornamos todos los objetos que se encuentran en el modelo alumnos
            return render(request,"cursos/opiniones.html",{'comentarios':comentarios})
        else:
            messages.error(request,"Error al procesar el Formulario")    
    form = ComentarioContactoform()
    return render(request,'cursos/opiniones.html',{'form':form})



def opiniones(request):
        comentarios=ComentarioContacto.objects.all()# Indicamos que retornamos todos los objetos que se encuentran en el modelo alumnos
        return render(request,"cursos/opiniones.html",{'comentarios':comentarios})



def administrador(request):
      return render(request,"cursos/administrador.html")



def eliminarComentarioContacto(request, id, confirmacion='cursos/confirmareliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    comentarios=ComentarioContacto.objects.all()
    if request.method=='POST':
        comentario.delete()
        return render(request,"cursos/opiniones.html",{'comentarios':comentarios})
    return render(request, confirmacion, {'object':comentario})


def addcurso(request):
    alumnos=User.objects.filter(username = 'jesus').count()   

    if alumnos == 0:
        return render(request,"cursos/addcurso.html",{'mensaje':'No existe aun'})
    else:
        return render(request,"cursos/addcurso.html",{'mensaje':'Este correo ya fue utilizado'})



def registrar_curso(request):
    if request.method == 'POST':
        form = Cursoform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            cursos=Cursos.objects.all()# Indicamos que retornamos todos los objetos que se encuentran en el modelo alumnos
            return render(request,"cursos/cursos.html",{'cursos':cursos})
        else:
            messages.error(request,"Error al procesar el Formulario")  
            
    form = Cursoform()
    #return render(request,'cursos/registrar_solicita.html',{'form':form})
    cursos=Cursos.objects.all()# Indicamos que retornamos todos los objetos que se encuentran en el modelo alumnos
    return render(request,"cursos/cursos.html",{'cursos':cursos})
 
def eliminarCurso(request, id, confirmacion='cursos/confirmareliminacioncurso.html'):
    curso = get_object_or_404(Cursos, id=id)
    cursos=Cursos.objects.all()
    if request.method=='POST':
        curso.delete()
        
        return render(request,"cursos/cursos.html",{'cursos':cursos})
    else:
        messages.error(request,"Error al procesar el Formulario")  
        # Indicamos que retornamos todos los objetos que se encuentran en el modelo alumnos
    return render(request, confirmacion, {'object':curso})


def ConsultaIndividual(request, id):
    
    curso = Cursos.objects.get(id=id)
    #Get permite establecer  
    return render(request,'cursos/editarcurso.html',{'curso':curso})


def editar_Curso(request,id):
    curso = get_object_or_404(Cursos, id=id)
    form = Cursoform(request.POST,request.FILES, instance=curso)
    cursos=Cursos.objects.all()
    if form.is_valid():
        form.save()
        #Indicamos que retornamos todos los objetos que se encuentran en el modelo alumnos
        return render(request,"cursos/cursos.html",{'cursos':cursos})
            #Definimos que cuando guarde el comentario se vaya a la pagina donde consulta los comentarios contacto
    return render(request,"cursos/editar_curso.html",{'curso':curso})



def registrate(request):
    usuarios=''
    return render(request,"cursos/registrate.html",{'mensaje':usuarios})


def Registrar_usuario(request):
    correo = request.POST['correo']
    nombre = request.POST['nombre']
    password = request.POST['password']
    password2 = request.POST['password2']

    apellido = request.POST['apellido']
    alumnos=User.objects.filter(username = correo).count()   

    if alumnos == 0:
        if request.method=='POST':
            if password == password2:
                user = User.objects.create_user(correo, correo, password)
                user.first_name = nombre
                user.last_name = apellido
                user.save()
            else:
                return render(request,"cursos/registrate.html",{'mensaje':'Las Contraseñas no coinciden'})
        else: 
            return render(request,"cursos/registrate.html",{'mensaje':'Error en el Formulario'}) 
    else:
        return render(request,"cursos/registrate.html",{'mensaje':'Este correo ya fue utilizado'})

    return render(request,"cursos/login.html")   
