# Generated by Django 2.1 on 2018-08-15 19:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 15, 19, 23, 31, 886715, tzinfo=utc)),
        ),
    ]
