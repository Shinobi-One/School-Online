# Generated by Django 4.1 on 2023-06-04 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_module', '0002_teachers_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='slug',
            field=models.SlugField(default='', max_length=200, unique=True, verbose_name='عنوان در URL'),
        ),
    ]
