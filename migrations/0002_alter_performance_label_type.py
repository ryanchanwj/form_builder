# Generated by Django 3.2 on 2021-05-20 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_builder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='label_type',
            field=models.CharField(max_length=18),
        ),
    ]