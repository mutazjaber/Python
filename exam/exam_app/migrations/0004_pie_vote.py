# Generated by Django 4.2.7 on 2023-12-25 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0003_pie_delete_sighting'),
    ]

    operations = [
        migrations.AddField(
            model_name='pie',
            name='vote',
            field=models.ManyToManyField(related_name='voted_pies', to='exam_app.user'),
        ),
    ]
