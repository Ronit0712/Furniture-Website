# Generated by Django 5.0.3 on 2024-03-30 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0013_bgc1model_bgc2model_bgc3model_bgc4model_bslidermodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abtitle', models.CharField(max_length=100)),
                ('abdis', models.TextField()),
            ],
        ),
    ]