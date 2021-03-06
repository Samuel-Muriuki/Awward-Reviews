# Generated by Django 4.0.3 on 2022-04-12 08:13

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awarding', '0005_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/samm-gallery/image/upload/v1649751098/Ninja_fjh4xm.png', max_length=255, verbose_name='image'),
        ),
    ]
