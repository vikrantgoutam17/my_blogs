# Generated by Django 2.2.1 on 2019-06-02 18:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0033_auto_20190602_2332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 3, 0, 26, 54, 358620), verbose_name='date published'),
        ),
    ]
