# Generated by Django 5.0.7 on 2024-07-26 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='title',
            new_name='role',
        ),
    ]
