# Generated by Django 4.0.6 on 2022-08-07 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0019_remove_subscribdb_payable_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primedb',
            name='Subscription',
            field=models.BooleanField(null=True),
        ),
    ]
