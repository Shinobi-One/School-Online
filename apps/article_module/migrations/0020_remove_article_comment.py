# Generated by Django 3.2.20 on 2023-08-02 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0019_comments_article_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='comment',
        ),
    ]