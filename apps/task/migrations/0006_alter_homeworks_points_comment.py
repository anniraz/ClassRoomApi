# Generated by Django 4.1.7 on 2023-02-25 15:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0005_remove_task_points_homeworks_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeworks',
            name='points',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('to_homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.homeworks')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
