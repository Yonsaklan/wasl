# Generated by Django 5.0.1 on 2024-02-10 21:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('The_Owner', '0008_rename_image_project_images_alter_project_created_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='images',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='project',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
