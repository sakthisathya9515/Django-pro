# Generated by Django 4.0.6 on 2022-07-25 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0015_nonsubscribdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nonsubscribdb',
            old_name='onlyfeast_mode',
            new_name='onlyfeast',
        ),
        migrations.RenameField(
            model_name='subscribdb',
            old_name='subscribtion_mode',
            new_name='subscribtion',
        ),
    ]
