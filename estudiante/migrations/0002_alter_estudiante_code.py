# Generated by Django 4.0 on 2021-12-10 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiante', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='code',
            field=models.IntegerField(),
        ),
    ]
