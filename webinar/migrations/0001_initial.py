# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=220)),
                ('description', models.CharField(max_length=200)),
                ('duration', models.DateTimeField(verbose_name=b'duration of the course')),
                ('start_date', models.DateTimeField(verbose_name=b'start date')),
                ('image', models.ImageField(upload_to=b'/courses')),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=220)),
                ('image', models.ImageField(upload_to=b'/institute')),
                ('about', models.CharField(max_length=200)),
                ('courses', models.ForeignKey(to='webinar.Courses')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('teacher_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='courses',
            name='teacher',
            field=models.ForeignKey(to='webinar.Teacher'),
        ),
    ]
