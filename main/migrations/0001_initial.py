# Generated by Django 5.0.6 on 2024-06-27 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainPageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_image', models.ImageField(upload_to='header/', verbose_name='Header image')),
                ('title', models.CharField(max_length=500, verbose_name='Title on the main page')),
                ('content', models.TextField(verbose_name='Text on the main page')),
            ],
            options={
                'verbose_name': 'Main page content',
                'verbose_name_plural': 'Main page content',
            },
        ),
    ]
