# Generated by Django 4.2.7 on 2023-11-26 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books_Authors_app', '0002_rename_authors_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='Author', to='Books_Authors_app.book'),
        ),
    ]