# Generated by Django 2.2.1 on 2019-06-02 11:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0028_auto_20190602_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 2, 17, 22, 38, 103504), verbose_name='date published'),
        ),
    ]
