# Generated by Django 5.0.7 on 2024-07-28 03:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0003_rename_date_created_role_created_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='users',
            field=models.ManyToManyField(blank=True, default='Unassigned', related_name='roles', to=settings.AUTH_USER_MODEL),
        ),
    ]
