# Generated by Django 4.2.7 on 2023-11-23 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0004_alter_ninjas_dojo'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
