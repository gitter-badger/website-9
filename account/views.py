from django.shortcuts import render
from django.http import HttpResponse

# User auth
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login

# Models import 
from django.contrib.auth.models import User

# Form import 
from .forms import UserForm, LoginForm

# Random Username
from random import choice
from string import ascii_lowercase, digits

def generate_random_username(length=16, chars=ascii_lowercase+digits, split=4, delimiter='-'):
    
    username = ''.join([choice(chars) for i in xrange(length)])
    
    if split:
        username = delimiter.join([username[start:start+split] for start in range(0, len(username), split)])
    
    try:
        User.objects.get(username=username)
        return generate_random_username(length=length, chars=chars, split=split, delimiter=delimiter)
    except User.DoesNotExist:
        return username;

# Create your views here.
def signup(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			User = get_user_model()
			username = generate_random_username()
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			new = User.objects.create_user(username, email, password)
			new.first_name = form.cleaned_data['first_name']
			new.last_name = form.cleaned_data['last_name']
			new.save()
		else:
			print form.errors
	else:
		form = UserForm()
	return render(request, 'signup.html', {'form':form})


def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			
			getUserNameObj = User.objects.get(email=email)
			getUserName = getUserNameObj.username
			user = authenticate(username=getUserName, password=password)
			print getUserNameObj.is_active()
			if user:
				if user.is_active():
					login(request, user)
					return HttpResponseRedirect(reverse('frontend:home'))
				else:
					return HttpResponse('Your Account is invalid')
		else:
			print form.errors
	return render(request, 'login.html')

