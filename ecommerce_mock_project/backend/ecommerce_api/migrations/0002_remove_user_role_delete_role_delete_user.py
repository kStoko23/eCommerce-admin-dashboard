# Generated by Django 5.0.6 on 2024-06-26 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
