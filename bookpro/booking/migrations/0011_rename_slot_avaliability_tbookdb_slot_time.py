# Generated by Django 4.0.6 on 2022-07-25 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_tbookdb_alter_primedb_subscription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbookdb',
            old_name='Slot_Avaliability',
            new_name='Slot_time',
        ),
    ]