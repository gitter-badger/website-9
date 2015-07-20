from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
	PROFILE_TYPE = (
		('ST', 'Students'),
		('IN', 'Institute'),
	)
	profile_type = models.CharField(max_length=2, choices=PROFILE_TYPE)
	age = models.DateField('age')
	phone_number = models.IntegerField()