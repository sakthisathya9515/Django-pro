# Generated by Django 4.0.6 on 2022-08-12 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0021_alter_primedb_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribdb',
            name='payable',
            field=models.IntegerField(default=310),
        ),
        migrations.AlterField(
            model_name='primedb',
            name='Subscription',
            field=models.IntegerField(choices=[(1, 'Subscription'), (2, 'nonSubscription')], default=0),
        ),
        migrations.AlterField(
            model_name='subscribdb',
            name='Contribution',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
