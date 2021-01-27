# Generated by Django 3.1.5 on 2021-01-27 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20210127_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='short_description',
            field=models.TextField(blank=True, max_length=1024),
        ),
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.TextField(blank=True, max_length=1024),
        ),
    ]