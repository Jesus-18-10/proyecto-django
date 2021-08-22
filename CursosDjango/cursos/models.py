from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.fields import TextField
from django.db.models.manager import Manager
#Creamos el modelo de datos

class Cursos(models.Model):#Define la estructura de nuestra tabla
    nombre = models.CharField(max_length=30, verbose_name="Nombre")#Texto corto, Con verbose_name cambiamos el nombre a visualizar
    descripcion = models.TextField(verbose_name="Descripción")#texto largo
    precio = models.IntegerField(verbose_name="Costo")
    duracion_horas = models.IntegerField(verbose_name="Duración en Horas")
    asesor = models.CharField(max_length=30,verbose_name="Nombre del asesor")#Texto corto
    correo_asesor = models.EmailField(verbose_name="Correo del asesor")
    descuento = models.BooleanField(verbose_name="Contiene Descuento?")
    porcentaje_descuento = models.DecimalField(max_digits=4,decimal_places=2,default=00.00 ,verbose_name="Descuento Con decimales")
    imagen = models.ImageField(null = True, upload_to="fotos", verbose_name="Fotografia")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creación")#Fecha y hora
    updated = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Actualización")
  
    class Meta:
        verbose_name = "Cursos"#Nombre en singular
        verbose_name_plural = "Cursos"#Nombre en plural
        ordering = ["-created"]#Ordenamos de la más antigua a la mas reciente -created
    def __str__(self):
        return self.nombre#Retorna el nombre para mostrar


class Solicita_informacion(models.Model):#Define la estructura de nuestra tabla
    id = models.AutoField(primary_key=True,verbose_name="Clave")#Texto corto
    usuario = models.CharField(max_length=25, verbose_name="Nombre (s)")#texto largo
    apellidos = models.CharField(max_length=30, verbose_name="Apellidos")#texto largo
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")#Fecha y hora
    updated = models.DateTimeField(auto_now_add=True, verbose_name="Actualizadoo")#Fecha y hora
    estudiante = models.BooleanField(verbose_name="Es Estudiante?")
    correo = models.EmailField(verbose_name="Correo Electronico")
    telefono = models.CharField(max_length=10, verbose_name="Telefono")
    cursodeinteres = models.ForeignKey(Cursos,on_delete=models.CASCADE,verbose_name="Curso")
    mensaje = models.TextField(verbose_name="Comentario")
    calificacion = models.IntegerField(verbose_name="Calificacion para el sistio Web",default=0)
    class Meta:
        verbose_name = "Solicitud de Informacion"
        verbose_name_plural = "Solicitudes de Informacion"
        ordering = ["-created"]
    def __str__(self):
        return self.usuario

class ComentarioContacto(models.Model):#Define la estructura de nuestra tabla
    id = models.AutoField(primary_key=True,verbose_name="Clave")#Texto corto
    usuario = models.CharField(max_length=25,verbose_name="Usuario")#texto largo
    apellido = models.CharField(max_length=30,verbose_name="Apellido")
    mensaje = TextField(verbose_name="Comentario")
    estudiante = models.BooleanField(verbose_name="Eres Estudiante?")
    imagen = models.ImageField(null = True, upload_to="fotos_opiniones", verbose_name="Fotografia")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")#Fecha y hora
    class Meta:
        verbose_name = "Opinion"
        verbose_name_plural = "Opiniones"
        ordering = ["-created"]
    def __str__(self):
        return self.mensaje