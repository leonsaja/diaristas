# Generated by Django 3.2.6 on 2021-09-23 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_cidadeatendimento'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CidadeAtendimento',
            new_name='CidadesAtendimento',
        ),
    ]
