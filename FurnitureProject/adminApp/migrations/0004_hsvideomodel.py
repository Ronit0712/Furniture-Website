# Generated by Django 5.0.3 on 2024-03-28 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0003_htopicmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='HsvideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hsvideo', models.FileField(upload_to='static/images/')),
            ],
        ),
    ]
