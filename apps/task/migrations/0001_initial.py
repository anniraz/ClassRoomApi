# Generated by Django 4.1.7 on 2023-02-17 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttachToTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='task/')),
                ('files', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('instructions', models.TextField()),
                ('points', models.PositiveIntegerField(default=100)),
                ('subject', models.CharField(blank=True, max_length=100, null=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
