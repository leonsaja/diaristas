# Generated by Django 3.2.6 on 2021-10-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0003_alter_servico_icone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(blank=True, choices=[('twf-cleaning-1', 'twf-cleaning-1'), ('twf-cleaning-2', 'twf-cleaning-2'), ('twf-cleaning-3', 'twf-cleaning-3')], max_length=14),
        ),
    ]
