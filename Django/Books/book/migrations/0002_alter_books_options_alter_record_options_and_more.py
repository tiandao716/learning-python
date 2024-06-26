# Generated by Django 4.2.5 on 2023-10-06 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': '图书表', 'verbose_name_plural': '图书表'},
        ),
        migrations.AlterModelOptions(
            name='record',
            options={'verbose_name': '借还记录表', 'verbose_name_plural': '借还记录表'},
        ),
        migrations.AlterField(
            model_name='books',
            name='status',
            field=models.BooleanField(blank=True, default=False, verbose_name='是否出借'),
        ),
        migrations.AlterField(
            model_name='record',
            name='e_time',
            field=models.DateTimeField(auto_now=True, verbose_name='还书时间'),
        ),
        migrations.AlterField(
            model_name='record',
            name='s_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='借书时间'),
        ),
    ]
