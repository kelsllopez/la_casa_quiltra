# Generated by Django 5.1.7 on 2025-03-26 20:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animales', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del animal.', max_length=100)),
                ('edad', models.IntegerField(help_text='Edad aproximada en años si no se conoce la fecha de nacimiento.')),
                ('raza', models.CharField(help_text='Raza del animal si aplica.', max_length=100)),
                ('sexo', models.CharField(choices=[('Macho', 'Macho'), ('Hembra', 'Hembra')], help_text='Sexo del animal.', max_length=10)),
                ('tamano', models.CharField(choices=[('Pequeño', 'Pequeño'), ('Mediano', 'Mediano'), ('Grande', 'Grande')], help_text='Tamaño del animal.', max_length=10)),
                ('descripcion', models.TextField(help_text='Descripción general del animal, incluyendo su personalidad y necesidades especiales.')),
                ('ubicacion', models.CharField(help_text='Ubicación actual del animal, por ejemplo: refugio central.', max_length=100)),
                ('disponible', models.BooleanField(default=True, help_text='Indica si el animal está disponible para adopción.')),
                ('estado', models.CharField(choices=[('En adopción', 'En adopción'), ('Adoptado', 'Adoptado'), ('En tratamiento', 'En tratamiento')], default='En adopción', help_text='Estado actual del animal en el refugio.', max_length=20)),
                ('fecha_ingreso', models.DateField(auto_now_add=True, help_text='Fecha en la que el animal ingresó al refugio.')),
                ('vacunado', models.BooleanField(default=False, help_text='Indica si el animal tiene sus vacunas al día.')),
                ('esterilizado', models.BooleanField(default=False, help_text='Indica si el animal ha sido esterilizado/castrado.')),
                ('estado_salud', models.TextField(help_text='Información sobre la salud del animal.')),
                ('notas_adicionales', models.TextField(blank=True, help_text='Notas adicionales o comentarios sobre el animal.', null=True)),
                ('creado_el', models.DateTimeField(auto_now_add=True, help_text='Fecha y hora de creación del especie.')),
                ('actualizado_el', models.DateTimeField(auto_now=True, help_text='Fecha y hora de última modificación del especie.')),
                ('actualizado_por', models.ForeignKey(help_text='Usuario que modificó el especie.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animal_actualizado_por', to=settings.AUTH_USER_MODEL)),
                ('creado_por', models.ForeignKey(help_text='Usuario que creó el especie.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animal_creado_por', to=settings.AUTH_USER_MODEL)),
                ('especie', models.ForeignKey(help_text='Especie a la que pertenece el animal.', on_delete=django.db.models.deletion.CASCADE, to='animales.especie')),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(help_text='Imagen del animal.', upload_to='animales/')),
                ('galeria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='animales.animal')),
            ],
        ),
    ]
