# Generated by Django 3.2.20 on 2023-08-02 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0020_remove_article_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='عنوان دسته بندی')),
                ('url_title', models.URLField(verbose_name='عنوان دسته بندی در url')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده / نشده')),
            ],
        ),
    ]
