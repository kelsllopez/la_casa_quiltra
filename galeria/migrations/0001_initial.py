# Generated by Django 5.1.7 on 2025-03-28 00:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingresa el nombre de la imagen o galería.', max_length=255)),
                ('descripcion', models.TextField(blank=True, help_text='Descripción de la imagen (opcional).', null=True)),
                ('fecha', models.DateField(help_text='La fecha de la imagen .')),
                ('creado_el', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora de creación del especie.')),
                ('actualizado_el', models.DateTimeField(auto_now=True, help_text='Fecha y hora de última modificación del especie.')),
                ('actualizado_por', models.ForeignKey(help_text='Usuario que modificó la galeria.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='galeria_actualizado_por', to=settings.AUTH_USER_MODEL)),
                ('creado_por', models.ForeignKey(help_text='Usuario que creó la galeria.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='galeria_creado_por', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(help_text='Sube la imagen para la galería.', upload_to='galeria/')),
                ('galeria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='galeria.galeria')),
            ],
        ),
    ]
