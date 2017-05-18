#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse

# Create your views here.

def login_user(request):
  form = LoginForm()

  if request.method == "POST":

    form = LoginForm(request.POST)

    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]

        user = authenticate(username=username,password=password)

        if user:
            login(request, user)
        else:
            error = True
    else:
        form = LoginForm()

  return render(request, 'oauth/login.html', locals())

def logout_user(request):
  logout(request)
  return redirect(reverse('login'))

def hello(request):
  if request.user.is_authenticated():
    return HttpResponse("Hello {0} ".format(request.user.username))
  return HttpResponse("Tu n'es pas connecté.")