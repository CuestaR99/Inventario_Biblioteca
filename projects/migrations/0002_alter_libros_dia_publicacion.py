# Generated by Django 4.2.5 on 2023-09-07 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='dia_publicacion',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]