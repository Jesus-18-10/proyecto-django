# Generated by Django 3.2.4 on 2021-07-06 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0006_auto_20210706_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opiniones',
            name='id',
            field=models.CharField(max_length=12, primary_key=True, serialize=False, verbose_name='Clave'),
        ),
        migrations.AlterField(
            model_name='opiniones',
            name='usuario',
            field=models.CharField(max_length=12, verbose_name='Usuario'),
        ),
    ]