# Generated by Django 4.2.7 on 2023-11-26 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Books_Authors_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Authors',
            new_name='Author',
        ),
    ]