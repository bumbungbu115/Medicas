# Generated by Django 3.2.9 on 2021-11-30 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Medicas', '0020_delete_specialty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advisor_profile',
            old_name='spec',
            new_name='specialty',
        ),
    ]
