# Generated by Django 2.2.1 on 2019-06-04 20:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0071_auto_20190605_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 5, 2, 13, 54, 430764)),
        ),
    ]