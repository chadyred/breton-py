# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from blog.models import Commentaire, Article
from blog.forms import CommentaireForm
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib import messages

from django.contrib.auth.models import User as UserAuthModel

@login_required
@permission_required('blog.article.comment', raise_exception=True)
def comment_article(request, id):
    """FOnction qui permet de créé un commentaire"""
    form = CommentaireForm(request.POST or None)

    article = Article.objects.get(id=id)
    ajoute = False

    if form.is_valid() and article is not None:
        titre = form.cleaned_data["titre"]
        contenu = form.cleaned_data["contenu"]
        current_user = request.user

        commentaire = Commentaire()

        commentaire.titre = titre
        commentaire.contenu = contenu
        # commentaire.content_type = ContentType.objects.get(app_label="blog",model="article")
        # commentaire.object_id = article.id
        commentaire.content_object = article
        commentaire.user = UserAuthModel.objects.get(id=current_user.id).profile


        commentaire.save()
        messages.warning(request, "Commentaire bien ajouté !")

        return redirect('article_show', id=article.id)

    messages.warning(request, "Commentaire non ajouté !")

    return render(request, 'blog/article.html', locals())