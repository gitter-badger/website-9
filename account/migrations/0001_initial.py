# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_type', models.CharField(max_length=2, choices=[(b'ST', b'Students'), (b'IN', b'Institute')])),
                ('age', models.DateField(verbose_name=b'age')),
                ('phone_number', models.IntegerField()),
            ],
        ),
    ]
