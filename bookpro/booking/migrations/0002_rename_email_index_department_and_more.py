# Generated by Django 4.0.6 on 2022-07-20 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='index',
            old_name='email',
            new_name='Department',
        ),
        migrations.RenameField(
            model_name='index',
            old_name='first_name',
            new_name='First_name',
        ),
        migrations.RenameField(
            model_name='index',
            old_name='last_name',
            new_name='Last_name',
        ),
        migrations.AddField(
            model_name='index',
            name='Email',
            field=models.EmailField(default=0, max_length=254),
        ),
        migrations.AddField(
            model_name='index',
            name='Phoneno',
            field=models.IntegerField(default=0),
        ),
    ]
