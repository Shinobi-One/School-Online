# Generated by Django 4.2 on 2023-04-24 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='عنوان')),
                ('short_description', models.CharField(db_index=True, max_length=150, verbose_name='توضیحات کوتاه')),
                ('text', models.TextField()),
                ('slug', models.SlugField(blank=True, default='', max_length=200, unique=True, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال / غیرفعال')),
                ('date_added', models.DateField(auto_now=True, verbose_name='زمان انتشار')),
            ],
            options={
                'verbose_name': 'بلاگ',
                'verbose_name_plural': 'بلاگ ها',
            },
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'دوره', 'verbose_name_plural': 'دوره ها'},
        ),
    ]