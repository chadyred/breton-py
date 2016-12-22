# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField(null=False)
    date = models.DateTimeField( auto_now=True, auto_now_add=False, verbose_name="Date de parution")
    image = models.ImageField(upload_to="article/")
    nbVue = models.IntegerField(default=0)

    categorie = models.ForeignKey('Categorie')
    auteur = models.ForeignKey('User')

    def __str__(self):
        """
        Article de notre super blog !! intitulé
        """
        return self.titre

class Categorie(models.Model):
    label = models.TextField(max_length=150)

    def __str__(self):
        return self.label

class User(models.Model):
    username = models.TextField(max_length=255)
    # On fera eniteArticle.user_tag afin d'avoir les utilisateur qui ont taggé cette article
    articlesTag = models.ManyToManyField(Article, through="UserTagArticle", related_name="user_tag")


    def __str__(self):
        return self.username

class Tag(models.Model):
    libelle = models.TextField(max_length=100)
    article = models.ManyToManyField(Article,through="UserTagArticle")

    def __str__(self):
        return "#" + self.libelle

class UserTagArticle(models.Model):
    user = models.ForeignKey(User)
    tag = models.ForeignKey(Tag)
    article = models.ForeignKey(Article)

    def __str__(self):
        return "{0} à tagger : {1} sur l'article {2}".format(self.user, self.tag, self.article)

class Commentaire(models.Model):
    """Commentaire d'article"""

    titre = models.CharField(max_length=100, null=False)
    contenu = models.TextField(null=False)

    user = models.ForeignKey(User)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')

    def __str__(self):
        return "Commentaire {} sur l'article {} de {}".format(self.titre, self.article, self.user)