# Generated by Django 4.1.7 on 2023-02-18 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task', '0003_remove_task_owner_task_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachtotask',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='task/'),
        ),
        migrations.CreateModel(
            name='Homeworks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='homeworks/')),
                ('files', models.FileField(blank=True, null=True, upload_to='homeworks/')),
                ('time_published', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.task')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]