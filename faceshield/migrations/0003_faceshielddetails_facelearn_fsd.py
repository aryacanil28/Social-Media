# Generated by Django 3.2 on 2021-04-24 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faceshield', '0002_remove_faceshielddetails_facelearn_fsd'),
    ]

    operations = [
        migrations.AddField(
            model_name='faceshielddetails',
            name='facelearn_fsd',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='faceshield.facelearn'),
            preserve_default=False,
        ),
    ]
