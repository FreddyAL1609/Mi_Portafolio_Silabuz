# Generated by Django 4.1.3 on 2022-12-11 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0005_alter_portafolio_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portafolio',
            name='foto',
            field=models.ImageField(upload_to='albums/'),
        ),
    ]