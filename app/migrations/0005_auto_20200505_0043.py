# Generated by Django 3.0.5 on 2020-05-04 19:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200504_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogger',
            name='datePosted',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 4, 19, 13, 46, 792148, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='blogger',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
