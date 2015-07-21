# From python
from pprint import pprint

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Django extras
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# User auth
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Models import
from django.contrib.auth.models import User

# Form import
from .forms import UserForm, LoginForm

# Model import 
from .models import Profile

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
            try:
                user = User.objects.get(email=email)
                messages.warning(request, 'This email address already in use.')
                return HttpResponseRedirect(reverse('frontend:home'))
            except ObjectDoesNotExist:
                new = User.objects.create_user(username, email, password)
                new.first_name = form.cleaned_data['first_name']
                new.last_name = form.cleaned_data['last_name']
                new.save()
                # New Profile
                new_profile = Profile(user_id = new.id, profile_type=request.POST['type_class'])
                new_profile.save()
                messages.success(request, 'Your account created successfully.')
                return HttpResponseRedirect(reverse('frontend:home'))
    	else:
    		print form.errors
    else:
    	form = UserForm()
    return render(request, 'signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(username = user_obj.username, password=password)
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        messages.success(request, 'You are successfully logged in.')
                        return HttpResponseRedirect(reverse('accounts:user_detail'))
                    else:
                        return HttpResponse('Your Account is invalid')
                else:
                    messages.warning(request, 'You are use correct email/password.')
                    return HttpResponseRedirect(reverse('frontend:home'))
            except ObjectDoesNotExist:
                messages.warning(request, 'You are not created account.')
                return HttpResponseRedirect(reverse('frontend:home'))

        else:
            print form.errors
    else:
        return render(request, 'login.html')

def logout_view(request):
    messages.success(request, 'You are successfully logged out.')
    logout(request)
    return HttpResponseRedirect(reverse('frontend:home'))


def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)

@login_required(redirect_field_name='/account/login/')
def user_detail(request):
    profile = Profile.objects.get(user_id=request.user.id)
    return render(request, 'user-detail.html', {'profile':profile})
