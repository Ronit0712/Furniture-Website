# Generated by Django 5.0.3 on 2024-03-29 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0007_lslidermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='LvideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lvideo1', models.FileField(upload_to='static/images/')),
                ('lvideo2', models.FileField(upload_to='static/images/')),
            ],
        ),
    ]
