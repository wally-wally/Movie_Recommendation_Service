# Generated by Django 2.2.7 on 2019-11-22 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='followerse',
            new_name='followers',
        ),
    ]
