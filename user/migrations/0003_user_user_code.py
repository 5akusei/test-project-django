# Generated by Django 4.0.3 on 2022-04-20 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_code',
            field=models.CharField(default='', max_length=80, verbose_name='code'),
        ),
    ]
