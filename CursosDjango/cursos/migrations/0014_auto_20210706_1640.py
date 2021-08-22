# Generated by Django 3.2.4 on 2021-07-06 21:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0013_comentariocontacto_apellido'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentariocontacto',
            name='estudiante',
            field=models.BooleanField(default=False, verbose_name='Eres Estudiante?'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comentariocontacto',
            name='apellido',
            field=models.CharField(max_length=30, verbose_name='Apellido'),
        ),
        migrations.AlterField(
            model_name='comentariocontacto',
            name='mensaje',
            field=ckeditor.fields.RichTextField(verbose_name='Comentario'),
        ),
        migrations.AlterField(
            model_name='comentariocontacto',
            name='usuario',
            field=models.CharField(max_length=25, verbose_name='Usuario'),
        ),
    ]
