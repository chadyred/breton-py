 #-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.views.generic import ListView

# On import les vues de Django, avec un nom spécifique
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'crepes_bretonnes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/',views.login_user,name='login'),
	url(r'^connexion$', auth_views.login, {'template_name': 'oauth/generic/connexion.html'}),
    url(r'^logout/',views.logout_user,name='logout'),
    url(r'^hello/',views.hello,name='hello'),
]
