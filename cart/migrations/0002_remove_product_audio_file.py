# Generated by Django 3.1.2 on 2020-12-22 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='audio_file',
        ),
    ]
