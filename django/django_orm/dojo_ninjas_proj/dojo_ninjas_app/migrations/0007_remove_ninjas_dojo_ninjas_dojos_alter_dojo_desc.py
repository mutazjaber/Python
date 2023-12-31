# Generated by Django 4.2.7 on 2023-11-25 11:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0006_alter_dojo_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ninjas',
            name='dojo',
        ),
        migrations.AddField(
            model_name='ninjas',
            name='dojos',
            field=models.ForeignKey(default=datetime.datetime(2023, 11, 25, 11, 37, 22, 83944, tzinfo=datetime.timezone.utc), on_delete=django.db.models.deletion.CASCADE, related_name='ninja', to='dojo_ninjas_app.dojo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dojo',
            name='desc',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
