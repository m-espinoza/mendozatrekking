# Generated by Django 4.2.11 on 2024-03-28 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_destino_duracion_alter_album_autor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='destino',
            name='desnivel',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='destino',
            name='distancia',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='destino',
            name='tiempo',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
