# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_units'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.TextField(default='https://pbs.twimg.com/profile_images/674711558350475264/l9S59abp_400x400.jpg'),
            preserve_default=False,
        ),
    ]
