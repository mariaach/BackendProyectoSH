# Generated by Django 4.2.20 on 2025-07-12 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0002_mascota_foto_masc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='foto_masc',
            field=models.ImageField(blank=True, null=True, upload_to='mascotas/'),
        ),
    ]
