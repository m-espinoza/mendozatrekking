# Generated by Django 4.2.11 on 2024-03-28 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_inicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='posicion',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
