# Generated by Django 5.0.1 on 2024-06-02 23:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0016_feasibilitystudyrequest_feasibility_study'),
    ]

    operations = [
        migrations.AddField(
            model_name='feasibilitystudy',
            name='feasibility_study_request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='feasibility_studies', to='Chat.feasibilitystudyrequest'),
        ),
    ]
