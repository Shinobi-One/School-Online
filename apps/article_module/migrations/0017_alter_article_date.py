# Generated by Django 4.1 on 2023-06-10 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0016_alter_article_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='تاریخ مقاله'),
        ),
    ]