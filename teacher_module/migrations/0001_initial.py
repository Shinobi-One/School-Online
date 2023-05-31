# Generated by Django 4.1 on 2023-05-31 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=50, verbose_name='  نام و نام خانوادگی مدرس')),
                ('Expertise', models.CharField(max_length=25, verbose_name='مهارت')),
                ('NumberofCorses', models.IntegerField(verbose_name='تعداد دوره ها ')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال/غیرفعال')),
                ('About_teacher', models.TextField(verbose_name='درباره مدرس')),
                ('Image', models.ImageField(null=True, upload_to='teacher_images', verbose_name='عکس مدرس')),
            ],
            options={
                'verbose_name': 'مدرسین',
                'verbose_name_plural': 'مدرسین',
            },
        ),
    ]