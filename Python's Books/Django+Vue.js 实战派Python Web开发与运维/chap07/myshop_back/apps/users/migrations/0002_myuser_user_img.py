# Generated by Django 3.2 on 2023-01-08 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='user_img',
            field=models.ImageField(default='', upload_to='user_img', verbose_name='头像'),
        ),
    ]
