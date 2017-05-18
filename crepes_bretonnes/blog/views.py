# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import Article, Categorie
from .forms import ArticleForm, ArticleModelForm
from django.views.generic import ListView, DetailView, CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon blog !</h1>
              <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""

    return HttpResponse(text)

def accueil(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon blog !</h1>
              <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""

    return render(request, 'blog/accueil.html', locals())

def articles(request):
    articles = Article.objects.all()

    return render(request, 'blog/articles.html', {"articles" : articles})

def article(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'blog/article.html', {"article" : article})


def editArticleJson(request, id):
    """Fonction qui va permettre de mettre un jour une instance d'article"""

    form = createEditArticleForm(request, id)
    print(form)
    # contenu = request.POST.get("contenu")
    editer = False
    contenu = request.POST.get('contenu')

    print(contenu)
    if request.method == 'POST':
#         #POST goes here . is_ajax is must to capture ajax requests. Beginner's pit.
        if request.is_ajax():
            if form.is_valid():
                form.save()
                editer = True

    return JsonResponse({"resultat":editer})

@login_required(redirect_field_name="next-goto")
def createArticle(request):
    """FOnction qui permet de créé un article"""

    form = ArticleForm(request.POST or None, request.FILES)

    ajoute = False

    if form.is_valid():
        titre = form.cleaned_data["titre"]
        contenu = form.cleaned_data["contenu"]
        auteur = form.cleaned_data["auteur"]
        categorie = form.cleaned_data["categorie"]
        image = form.cleaned_data["image"]

        article = Article()

        article.titre = titre
        article.contenu = contenu
        article.auteur = auteur
        article.categorie = categorie
        article.image = image

        article.save()

        ajoute = True

    return render(request, 'blog/article_create.html', locals())


def createArticleFromModel(request):
    """FOnction qui permet de créé un article"""

    form = ArticleModelForm(request.POST or None, request.FILES)

    ajoute = False

    if form.is_valid():
        form.save()
        ajoute = True

    return render(request, 'blog/article_create_from_model.html', locals())

def createEditArticleForm(request, id):
    article = Article.objects.get(id=id)


    form = ArticleModelForm(request.POST or None, instance=article)

    return form


def editArticle(request, id):
    """Fonction qui va permettre de mettre un jour une instance d'article"""
    form = createEditArticleForm(request, id)

    editer = False

    if form.is_valid():
        form.save()
        editer = True

    return render(request, 'blog/article_edit.html', locals())

class ArticleListView(ListView):
    model = Article
    template_name = "blog/articleListView.html"
    context_object_name = "liste_articles"
    paginate_by = 5


    def get_context_data(self, **kwargs):
        """Permet de récupéré les catégorie avec les liens"""

        context = super(ArticleListView, self).get_context_data(**kwargs)

        # On enrichie le context avec les categories
        context['categories'] = Categorie.objects.all()

        return context

def deleteArticle(request, id):
    """FOnction qui permet de supprimer un article"""
    article = Article.objects.get(id=id)

    article.delete()

    return redirect("articles_list")

class ArticleByCategorieListView(ArticleListView):
    """Vue susvisé : blog/article_list.html, objet container : object_list"""

    def get_queryset(self):
        return Article.objects.filter(categorie__id=self.kwargs['id'])

class ArticleDetailView(DetailView):
    """Permet de voir un article (la pk est préciser dans l'url => id)"""

    model = Article
    template_name = "blog/article_show.html"
    context_object_name = "article"

    def get_object(self):
        """On récupère l'objet en cours de visionnage et on l'enrichie"""

        article = super(ArticleDetailView, self).get_object()

        article.nbVue += 1

        article.save()

        return article

# CRUD is here
class CreateArticleView(CreateView):
    """templatename n'est pas précisé = blog/article_create_form.html"""
    model = Article
    form_class = ArticleModelForm
    success_url = reverse_lazy(articles) # On redirige vers la fonction directement
