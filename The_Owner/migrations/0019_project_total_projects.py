# Generated by Django 5.0.1 on 2024-05-06 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('The_Owner', '0018_remove_project_total_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='total_projects',
            field=models.IntegerField(default=0),
        ),
    ]