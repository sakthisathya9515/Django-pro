# Generated by Django 4.0.6 on 2022-08-21 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0022_subscribdb_payable_alter_primedb_subscription_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primedb',
            name='Subscription',
            field=models.IntegerField(choices=[[1, 'Subscription'], [2, 'nonSubscription']], default=0),
        ),
        migrations.AlterField(
            model_name='subscribdb',
            name='payable',
            field=models.IntegerField(default=2500),
        ),
    ]