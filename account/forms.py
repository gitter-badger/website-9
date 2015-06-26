from django.forms import ModelForm

from django.contrib.auth.models import User

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['email', 'password', 'first_name', 'last_name']


class LoginForm(ModelForm):
	class Meta:
		model = User
		fields = ['email', 'password']