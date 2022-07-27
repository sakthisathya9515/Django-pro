# Generated by Django 4.0.6 on 2022-07-25 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_remove_tbookdb_slot_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbookdb',
            old_name='additionalpass',
            new_name='Additionalpass',
        ),
        migrations.RenameField(
            model_name='tbookdb',
            old_name='contribution',
            new_name='Contribution',
        ),
        migrations.RenameField(
            model_name='tbookdb',
            old_name='payable',
            new_name='Payable',
        ),
        migrations.AddField(
            model_name='tbookdb',
            name='Slot_time',
            field=models.IntegerField(blank=True, choices=[(1, '08:00 PM(40)'), (2, '08:30 PM(40)'), (3, '09:00 PM(20)'), (4, '09:30 PM(20)')], default=0),
        ),
    ]