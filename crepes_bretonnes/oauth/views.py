from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.

def login(request):
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
