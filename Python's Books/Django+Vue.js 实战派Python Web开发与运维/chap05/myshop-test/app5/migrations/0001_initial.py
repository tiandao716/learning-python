# Generated by Django 4.1.4 on 2022-12-11 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImgFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30, verbose_name='用户名称')),
                ('headimg', models.FileField(upload_to='uploads/', verbose_name='文件名')),
            ],
            options={
                'verbose_name': '头像信息',
                'db_table': 'user_img',
            },
        ),
    ]
