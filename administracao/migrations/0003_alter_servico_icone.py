# Generated by Django 3.2.6 on 2021-10-22 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0002_rename_service_servico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(blank=True, choices=[('twf-cleaning-1', 'teste'), ('twf-cleaning-2', 'twf-cleaning-2'), ('twf-cleaning-3', 'twf-cleaning-3')], max_length=14),
        ),
    ]