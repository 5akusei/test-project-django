# Generated by Django 4.0.4 on 2022-06-01 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zone',
            name='img_url',
        ),
    ]
