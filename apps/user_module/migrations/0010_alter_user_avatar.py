# Generated by Django 4.1.2 on 2023-06-10 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_module', '0009_merge_20230610_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='User-avatar', verbose_name='آواتار'),
        ),
    ]
