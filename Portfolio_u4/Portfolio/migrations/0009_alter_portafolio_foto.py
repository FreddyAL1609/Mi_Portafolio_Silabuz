# Generated by Django 4.1.3 on 2022-12-12 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0008_alter_portafolio_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portafolio',
            name='foto',
            field=models.URLField(max_length=100),
        ),
    ]