# Generated by Django 4.0.3 on 2022-04-26 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_user_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_code',
        ),
        migrations.AddField(
            model_name='user',
            name='user_active_code',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AddField(
            model_name='user',
            name='user_active_url_code',
            field=models.CharField(default='', max_length=60),
        ),
    ]
