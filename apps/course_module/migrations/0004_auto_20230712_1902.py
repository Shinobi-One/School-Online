# Generated by Django 3.2.20 on 2023-07-12 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course_module', '0003_alter_blog_date_added'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=300, verbose_name='عنوان')),
                ('url_title', models.CharField(db_index=True, max_length=300, verbose_name='عنوان در url')),
                ('is_active', models.BooleanField(verbose_name='فعال / غیرفعال')),
                ('is_delete', models.BooleanField(verbose_name='حذف شده / نشده')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='course_length',
            field=models.IntegerField(default='1', verbose_name='زمان دوره'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='lessons',
            field=models.IntegerField(default=1, verbose_name='تعداد دروس'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='user_module.user', verbose_name='مدرس دوره'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='CourseVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=25, verbose_name='آی پی کاربر')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_visit', to='course_module.course', verbose_name='دوره ')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='selected_categories',
            field=models.ManyToManyField(to='course_module.CourseCategory', verbose_name='دسته بندی ها '),
        ),
    ]
