# Generated by Django 2.2.1 on 2019-06-01 11:15

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0013_auto_20190601_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 16, 45, 56, 40953), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]