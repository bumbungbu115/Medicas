# Generated by Django 3.2.9 on 2021-11-26 11:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Medicas', '0010_merge_20211126_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='infosp',
            name='URL',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]
