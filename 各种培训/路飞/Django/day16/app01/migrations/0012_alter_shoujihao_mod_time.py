# Generated by Django 4.1.3 on 2022-12-05 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_remove_shoujihao_flag_shoujihao_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoujihao',
            name='mod_time',
            field=models.DateTimeField(db_index=True, verbose_name='修改时间'),
        ),
    ]
