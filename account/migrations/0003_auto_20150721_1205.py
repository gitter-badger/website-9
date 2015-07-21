# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20150721_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(null=True),
        ),
    ]
