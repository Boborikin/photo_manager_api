# Generated by Django 3.2.6 on 2022-12-18 11:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='upload_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]