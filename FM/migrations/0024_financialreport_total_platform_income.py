# Generated by Django 5.0.1 on 2024-06-09 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FM', '0023_financialmovement_feasibility_study_request_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialreport',
            name='total_platform_income',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]