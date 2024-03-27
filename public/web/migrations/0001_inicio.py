# Generated by Django 4.2.11 on 2024-03-27 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('foto_portada', models.CharField(max_length=255)),
                ('mapa', models.CharField(max_length=512)),
                ('como_llegar', models.TextField()),
                ('descripcion', models.TextField()),
                ('contacto', models.CharField(blank=True, max_length=255, null=True)),
                ('precaucion', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificado', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('foto', models.CharField(max_length=512)),
                ('coordenada', models.CharField(blank=True, max_length=512, null=True)),
                ('detalle', models.CharField(blank=True, max_length=128, null=True)),
                ('autor', models.CharField(blank=True, max_length=128, null=True)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('destino', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.destino')),
            ],
        ),
    ]
