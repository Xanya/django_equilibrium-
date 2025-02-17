# Generated by Django 5.0.6 on 2024-06-27 13:41

import image_cropping.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainpagecontent',
            name='crop_header_image',
            field=image_cropping.fields.ImageRatioField('header_image', '300x300', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='crop header image'),
        ),
    ]
