# Generated by Django 5.0.7 on 2024-07-28 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_title_customuser_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='role',
        ),
        migrations.AddField(
            model_name='customuser',
            name='title',
            field=models.CharField(default='Unassigned', max_length=30),
        ),
    ]
