# Generated by Django 5.0.2 on 2024-04-26 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UsuarioE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dpi', models.CharField(max_length=20)),
                ('contraseña', models.CharField(max_length=100)),
                ('confirmacion_contraseña', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioN',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('dpi', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateField()),
                ('telefono', models.CharField(max_length=15)),
                ('nombre_usuario', models.CharField(max_length=50)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('contraseña', models.CharField(max_length=100)),
                ('confirmacion_contraseña', models.CharField(max_length=100)),
            ],
        ),
    ]
