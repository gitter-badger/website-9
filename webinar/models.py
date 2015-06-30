from django.db import models

# Create your models here.

class Institute(models.Model):
    name = models.CharField(max_length=220)
    image = models.ImageField(upload_to='/institute')
    about = models.CharField(max_length=200)
    courses = models.ForeignKey('Courses')


class Courses(models.Model):
    title = models.CharField(max_length=220)
    description = models.CharField(max_length=200)
    teacher = models.CharField(max_length=200)
    duration = models.DateTimeField('duration of the course')
    start_date = models.DateTimeField('start date')
    image = models.ImageField(upload_to='/courses')
