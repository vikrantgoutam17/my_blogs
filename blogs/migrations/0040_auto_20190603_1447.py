# Generated by Django 2.2.1 on 2019-06-03 09:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0039_auto_20190603_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 3, 14, 47, 3, 622569), verbose_name='date published'),
        ),
    ]
