# Generated by Django 4.1 on 2023-04-25 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=False, max_length=255),
        ),
    ]
