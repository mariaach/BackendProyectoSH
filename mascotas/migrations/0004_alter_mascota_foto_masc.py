# Generated by Django 4.2.20 on 2025-07-12 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascotas', '0003_alter_mascota_foto_masc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='foto_masc',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
