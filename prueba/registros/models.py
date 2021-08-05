from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.fields import TextField


# Create your models here.
class Alumnos(models.Model):#Define la estructura de nuestra tabla
    matricula = models.CharField(max_length=12,verbose_name="Matricula")#Texto corto
    nombre = models.TextField(verbose_name="Nombre")#texto largo
    carrera = models.TextField(verbose_name="Carrera")
    turno = models.CharField(max_length=10)
    imagen = models.ImageField(null = True, upload_to="fotos", verbose_name="Fotografia")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Creación")#Fecha y hora
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha actualización") 
    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"
        ordering = ["-created"]
    def __str__(self):
        return self.nombre

class Comentario(models.Model):#Define la estructura de nuestra tabla
    id = models.AutoField(primary_key=True,verbose_name="Clave")#Texto corto
    alumno = models.ForeignKey(Alumnos,on_delete=models.CASCADE,verbose_name="Alumno")#texto largo
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")#Fecha y hora
    coment = RichTextField(verbose_name="Comentario")
    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-created"]
    def __str__(self):
        return self.coment

class ComentarioContacto(models.Model):#Define la estructura de nuestra tabla
    id = models.AutoField(primary_key=True,verbose_name="Clave")#Texto corto
    usuario = models.TextField(verbose_name="Usuario")#texto largo
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")#Fecha y hora
    mensaje = TextField(verbose_name="Comentario")
    class Meta:
        verbose_name = "Comentario Contacto"
        verbose_name_plural = "Comentarios Contactos"
        ordering = ["-created"]
    def __str__(self):
        return self.mensaje
        
class Archivos(models.Model):#Define la estructura de nuestra tabla
    id = models.AutoField(primary_key=True,verbose_name="Clave")#Texto corto
    titulo = models.CharField(max_length=100, verbose_name="Titulo")
    descripcion = models.TextField(null=True, blank=True)
    archivo = models.FileField(upload_to="archivos",null=True, blank=True, verbose_name="Archivos")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha que fue Registrado")
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Fecha actualización") 

    class Meta:
        verbose_name = "Archivo"
        verbose_name_plural = "Archivos"
        ordering = ["-created"]
    def __str__(self):
        return self.titulo