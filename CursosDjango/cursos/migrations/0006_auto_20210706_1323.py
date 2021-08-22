# Generated by Django 3.2.4 on 2021-07-06 18:23

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0005_comentariocontacto'),
    ]

    operations = [
        migrations.CreateModel(
            name='opiniones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('usuario', models.TextField(verbose_name='Usuario')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Registrado')),
                ('mensaje', ckeditor.fields.RichTextField(verbose_name='Comentario')),
            ],
            options={
                'verbose_name': 'Opiniones Contacto',
                'verbose_name_plural': 'Opiniones Contactos',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterField(
            model_name='comentariocontacto',
            name='apellidos',
            field=models.CharField(max_length=30, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='comentariocontacto',
            name='usuario',
            field=models.CharField(max_length=25, verbose_name='Nombre (s)'),
        ),
    ]
