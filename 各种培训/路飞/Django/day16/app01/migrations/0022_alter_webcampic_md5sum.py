# Generated by Django 4.1.3 on 2022-12-09 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0021_webcampic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webcampic',
            name='md5sum',
            field=models.CharField(max_length=32, unique=True, verbose_name='MD5值'),
        ),
    ]
