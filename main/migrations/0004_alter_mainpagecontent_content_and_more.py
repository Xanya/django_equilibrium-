# Generated by Django 5.0.6 on 2024-06-27 14:35

import ckeditor.fields
import image_cropping.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_mainpagecontent_header_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpagecontent',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Text on the main page'),
        ),
        migrations.AlterField(
            model_name='mainpagecontent',
            name='crop_header_image',
            field=image_cropping.fields.ImageRatioField('header_image', '500x500', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='crop header image'),
        ),
    ]
