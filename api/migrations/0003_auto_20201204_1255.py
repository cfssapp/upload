# Generated by Django 3.0.3 on 2020-12-04 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201204_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='href',
        ),
        migrations.RemoveField(
            model_name='task',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='task',
            name='subDescription',
        ),
        migrations.AddField(
            model_name='task',
            name='completed',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
