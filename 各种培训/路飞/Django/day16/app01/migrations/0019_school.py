# Generated by Django 4.1.3 on 2022-12-08 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0018_webcam_file_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=12)),
            ],
        ),
    ]
