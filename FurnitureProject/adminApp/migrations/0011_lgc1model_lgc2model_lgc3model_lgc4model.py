# Generated by Django 5.0.3 on 2024-03-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0010_lsvideomodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lgc1Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lgc1img', models.ImageField(upload_to='static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Lgc2Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lgc2img', models.ImageField(upload_to='static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Lgc3Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lgc3img', models.ImageField(upload_to='static/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Lgc4Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lgc4img', models.ImageField(upload_to='static/images/')),
            ],
        ),
    ]