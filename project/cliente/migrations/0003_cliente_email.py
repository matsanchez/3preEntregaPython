# Generated by Django 4.2.7 on 2023-12-05 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_idioma_cliente_idioma'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]
