# Generated by Django 5.0.7 on 2024-07-27 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='department',
            old_name='date_created',
            new_name='created_at',
        ),
    ]
