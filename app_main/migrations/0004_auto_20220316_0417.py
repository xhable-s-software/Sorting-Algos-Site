# Generated by Django 2.2.17 on 2022-03-16 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0003_auto_20220315_1910'),
    ]

    operations = [
        migrations.RenameField(
            model_name='algorithm',
            old_name='sort_percent',
            new_name='sort_percentage',
        ),
    ]
