# Generated by Django 3.2.5 on 2021-09-10 13:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210910_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png', 'bmp'])]),
        ),
        migrations.AlterField(
            model_name='news',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos_uploaded', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mov', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]
