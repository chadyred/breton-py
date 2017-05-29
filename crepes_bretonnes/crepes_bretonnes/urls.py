from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from blog import views as blog_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'crepes_bretonnes.views.home', name='home'),
    url(r'^$', TemplateView.as_view(template_name='blog/accueil.html')),
    url(r'accueil$', blog_views.accueil, name="accueil"),
    url(r'^blog/', include('blog.urls')),
    url(r'^oauth/', include('oauth.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^newletter$', TemplateView.as_view(template_name='blog/staticView.html')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^language$', blog_views.language, name="languages"),
    url(r'^pages/', include('django.contrib.flatpages.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)