# Generated by Django 4.1.7 on 2023-02-23 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_alter_attachtotask_files_homeworks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='points',
        ),
        migrations.AddField(
            model_name='homeworks',
            name='points',
            field=models.PositiveIntegerField(default=100),
        ),
    ]
