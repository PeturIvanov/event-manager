# Generated by Django 4.2.4 on 2023-08-16 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_data',
            new_name='event_date',
        ),
    ]
