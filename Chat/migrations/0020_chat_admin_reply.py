# Generated by Django 5.0.1 on 2024-06-03 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0019_alter_chat_admin_alter_chat_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='admin_reply',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
