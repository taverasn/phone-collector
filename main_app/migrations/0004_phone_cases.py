# Generated by Django 3.1.6 on 2021-02-18 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_usage'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='cases',
            field=models.ManyToManyField(to='main_app.Case'),
        ),
    ]
