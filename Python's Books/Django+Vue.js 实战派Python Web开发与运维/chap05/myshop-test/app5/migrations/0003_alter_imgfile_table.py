# Generated by Django 4.1.4 on 2022-12-11 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app5', '0002_alter_imgfile_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='imgfile',
            table='user_img',
        ),
    ]
