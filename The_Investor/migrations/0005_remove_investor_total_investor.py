# Generated by Django 5.0.1 on 2024-05-06 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('The_Investor', '0004_investor_total_investor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investor',
            name='total_investor',
        ),
    ]