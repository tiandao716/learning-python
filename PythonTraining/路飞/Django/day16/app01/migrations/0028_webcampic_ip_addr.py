# Generated by Django 4.1.4 on 2022-12-12 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0027_alter_webcampic_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='webcampic',
            name='ip_addr',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
