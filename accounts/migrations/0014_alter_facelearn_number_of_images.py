# Generated by Django 3.2 on 2021-04-18 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_facelearn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facelearn',
            name='number_of_images',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
