# Generated by Django 3.2.6 on 2021-10-02 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_usuario_telefone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='username',
        ),
    ]
