# Generated by Django 3.2 on 2021-04-18 12:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0010_auto_20210418_1733'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shield',
            options={'verbose_name_plural': 'Shield Details'},
        ),
        migrations.AddField(
            model_name='shield',
            name='active',
            field=models.BooleanField(default=False, verbose_name='active'),
        ),
        migrations.AddField(
            model_name='shield',
            name='pending',
            field=models.BooleanField(default=False, verbose_name='pending'),
        ),
        migrations.AddField(
            model_name='shield',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
