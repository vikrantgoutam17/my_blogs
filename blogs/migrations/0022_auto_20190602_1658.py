# Generated by Django 2.2.1 on 2019-06-02 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0021_auto_20190601_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 2, 16, 58, 6, 756277), verbose_name='date published'),
        ),
    ]
