# Generated by Django 4.1 on 2023-06-10 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0012_alter_comments_options_alter_comments_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='writer',
            field=models.CharField(default=None, max_length=255, verbose_name='نام و نام خانوادگی نویسنده '),
        ),
    ]
