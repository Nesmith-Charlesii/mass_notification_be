# Generated by Django 5.0.7 on 2024-07-27 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0002_rename_user_role_users_role_date_created_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='date_created',
            new_name='created_at',
        ),
    ]