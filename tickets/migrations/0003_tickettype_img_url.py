# Generated by Django 4.0.4 on 2022-06-01 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_alter_ticket_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickettype',
            name='img_url',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
