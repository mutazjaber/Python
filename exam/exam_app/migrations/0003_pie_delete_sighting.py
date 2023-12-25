# Generated by Django 4.2.7 on 2023-12-25 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0002_sighting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('filling', models.CharField(max_length=100)),
                ('crust', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('my_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cook', to='exam_app.user')),
            ],
        ),
        migrations.DeleteModel(
            name='Sighting',
        ),
    ]