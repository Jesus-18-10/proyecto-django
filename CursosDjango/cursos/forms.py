from django import forms
from django.db.models import fields
from .models import Cursos
from .models import ComentarioContacto
from .models import Solicita_informacion
from django.forms import ModelForm, ClearableFileInput, widgets

class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class ComentarioContactoform(ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ('usuario','apellido','mensaje','estudiante','imagen')
        
        widgets = {
            'imagen': CustomClearableFileInput
        }


class Cursoform(ModelForm):
    class Meta:
        model = Cursos
        fields = ('nombre','descripcion','precio','duracion_horas','asesor','correo_asesor','descuento','porcentaje_descuento','imagen')
        widgets = {
            'imagen': CustomClearableFileInput
        }

class Solicita_informacionform(forms.ModelForm):
    class Meta:
        model = Solicita_informacion
        fields = ['usuario','apellidos','estudiante','correo','telefono','cursodeinteres','mensaje','calificacion']

