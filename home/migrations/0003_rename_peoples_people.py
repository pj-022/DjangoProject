# Generated by Django 4.1.4 on 2022-12-14 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_users_peoples'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Peoples',
            new_name='People',
        ),
    ]