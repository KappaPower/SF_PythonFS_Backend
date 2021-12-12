# Generated by Django 3.2.6 on 2021-12-12 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamestock', '0003_auto_20211211_0116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='datetime_of_creation',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='datetime_of_creation',
            new_name='datetime',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='date_of_creation',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='time_of_creation',
        ),
        migrations.RemoveField(
            model_name='post',
            name='date_of_creation',
        ),
        migrations.RemoveField(
            model_name='post',
            name='date_of_last_update',
        ),
        migrations.RemoveField(
            model_name='post',
            name='datetime_of_last_update',
        ),
        migrations.RemoveField(
            model_name='post',
            name='time_of_creation',
        ),
        migrations.RemoveField(
            model_name='post',
            name='time_of_last_update',
        ),
    ]
