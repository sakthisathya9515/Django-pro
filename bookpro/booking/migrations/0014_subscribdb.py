# Generated by Django 4.0.6 on 2022-07-25 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_rename_additionalpass_tbookdb_additionalpass_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscribdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscribtion_mode', models.IntegerField(null=0)),
            ],
        ),
    ]
