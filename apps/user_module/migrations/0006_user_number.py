# Generated by Django 4.1.2 on 2023-06-07 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0005_user_about_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='شماره همراه'),
        ),
    ]
