# Generated by Django 3.2.6 on 2021-10-03 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(max_length=11, null=True),
        ),
    ]