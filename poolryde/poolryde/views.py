__author__ = 'Ryan Perkins'
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from userprofile.models import UserProfile

from .forms import MyRegistrationForm
from userprofile.forms import UserProfileForm


def login(request):

    token = {}
    token.update(csrf(request))
    return render_to_response('login.html', token)


def login_success(request):
    user_name = request.user.username
    acct = auth.models.User.objects.get(username=user_name)
    user = UserProfile.objects.get(pk=9)
    user_data_form = {}
    user_data_form["user_profile_detail"] = user
    user_data_form["user_acct_detail"] = acct
    return render_to_response('login_success.html', user_data_form)


def authenticate(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/login_success')
    else:
        return HttpResponseRedirect('/invalid')


def register(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form. is_valid():
            form.save()
            return HttpResponseRedirect('/register_success')

    else:
        form = MyRegistrationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('register.html', token)


def register_success(request):
    return render_to_response('register_success.html')


def invalid(request):
    return render_to_response('invalid.html')


def logout(request):
    auth.logout(request)
    token = {}
    token.update(csrf(request))
    return render_to_response('logout.html', token)

