from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.views.generic import ListView


urlpatterns = [
    # Examples:
    # url(r'^$', 'crepes_bretonnes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^accueil$', views.home, name="accueil"),
    url(r'^articles$', views.articles, name="articles_list"),
    url(r'^articles/(?P<id>\d+)/categorie/$', views.ArticleByCategorieListView.as_view(), name="article_by_categorie"),
    url(r'^articles-list-view$', views.ArticleListView.as_view(), name="articles_list_view"),
    url(r'^article/(?P<id>\d+)/\w{1,}$', views.article, name="article_show"),
    url(r'^article/create$', views.createArticle, name="article_create"),
    url(r'^article/create-from-model$', views.createArticleFromModel, name="article_create_from_model"),
    url(r'^article/create-from-views$', views.CreateArticleView.as_view(), name="article_create_from_views"),
    url(r'^article/edit/(?P<id>\d+)/json$', views.editArticleJson, name="article_edit_json"),
    url(r'^article/edit/(?P<id>\d+)$', views.editArticle, name="article_edit"),
    url(r'^article/(?P<pk>\d+)/show/$', views.ArticleDetailView.as_view(), name="article_show_view")
]
