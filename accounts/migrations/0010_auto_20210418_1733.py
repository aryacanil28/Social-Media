# Generated by Django 3.2 on 2021-04-18 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20210418_1731'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shield',
            options={},
        ),
        migrations.RemoveField(
            model_name='shield',
            name='active',
        ),
        migrations.RemoveField(
            model_name='shield',
            name='pending',
        ),
        migrations.RemoveField(
            model_name='shield',
            name='user',
        ),
    ]
