# Generated by Django 5.0 on 2024-05-14 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('The_Investor', '0011_investor_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='investmentrequest',
            name='investor_identifier',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]