# Generated by Django 4.1.2 on 2023-05-01 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0003_rename_massage_contactus_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='title',
            field=models.CharField(max_length=300, verbose_name='وبسایت'),
        ),
    ]