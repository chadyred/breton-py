from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.views.generic import ListView


urlpatterns = [
    # Examples:
    # url(r'^$', 'crepes_bretonnes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/',views.login,name='login')
]
