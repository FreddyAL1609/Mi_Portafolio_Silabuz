# Generated by Django 4.1.6 on 2023-02-15 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0009_alter_portafolio_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portafolio',
            name='foto',
            field=models.URLField(max_length=150),
        ),
        migrations.AlterField(
            model_name='portafolio',
            name='url',
            field=models.URLField(max_length=150),
        ),
    ]
