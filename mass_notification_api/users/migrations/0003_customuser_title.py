# Generated by Django 5.0.7 on 2024-07-26 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_groups_customuser_is_superuser_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='title',
            field=models.CharField(default='Unassigned', max_length=50),
        ),
    ]
