# Generated by Django 2.1.5 on 2021-06-26 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0002_pelicula_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='video',
            field=models.CharField(max_length=1050, null='true'),
        ),
    ]
