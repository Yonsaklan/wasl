# Generated by Django 5.0 on 2024-05-20 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('The_Investor', '0017_remove_investmentrequest_comment_and_more'),
        ('The_Owner', '0038_alter_owner_address_alter_owner_photo'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='investorratingcomment',
            unique_together={('investor', 'project')},
        ),
    ]