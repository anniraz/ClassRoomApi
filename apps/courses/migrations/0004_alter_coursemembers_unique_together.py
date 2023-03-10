# Generated by Django 4.1.7 on 2023-02-18 14:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0003_rename_students_coursemembers'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='coursemembers',
            unique_together={('user', 'course')},
        ),
    ]
