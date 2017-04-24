#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver, Signal # decorateur : permet de modifier la fonction

from django.contrib.auth.models import User as UserAuthModel

crepe_finie = Signal(providing_args=["nom", "adresse"]) #"crepeingredient"])


class Ingredient(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class CrepeIngredient(models.Model):
    quantite = models.FloatField()
    unite = models.TextField(max_length=15)

    crepe = models.ForeignKey('Crepe', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} de {}".format(self.quantite, self.unite, self.ingredient)


class Crepe(models.Model):
    nom = models.CharField(max_length=100)

    def crepe_termine(self, adresse):
        print("exec")
        crepe_finie.send(sender=self, nom=self.nom, adresse=adresse)

    def __str__(self):
        return self.nom

@receiver(crepe_finie)
def livre(instance, **kwargs):
    """Déclancher lorsque le crêpe est prête"""
    print(instance) # __str__ de l'instance
    print("A livrer pour l'adresse" + kwargs['adresse'])

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


@receiver(post_delete, sender=Article)
def post_delete_article(sender, instance, **kwargs):
    """Déclanché à chaque suppression d'article

    sender : Model utilisé
    instance: instance concerné (attention si supprimé, ne pas la réenregistré, car des suppression en cascade peuvent avoir eu lieu)
    kwargs: plusieurs information, tel que le using,
    """

    print("Article deleted avec l'id {}".format(instance.id))


@receiver(post_save, sender=Crepe)
def post_delete_article(sender, instance, **kwargs):
    """Déclanché à chaque suppression d'article

    sender : Model utilisé
    instance: instance concerné (attention si supprimé, ne pas la réenregistré, car des suppression en cascade peuvent avoir eu lieu)
    kwargs: plusieurs information, tel que le using,
    """

    print("Save crepe")
    instance.crepe_termine("Adresse utilisateur")

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


    article = models.ForeignKey('Article')

    def __str__(self):
        return "Commentaire {} sur l'article {} de {}".format(self.titre, self.article, self.user)

class Page(models.Model):
    url = models.URLField()
    nb_visit = models.IntegerField(default=1)

    def __str__(self, page):
        return self.url;

class Profile(models.Model):
    user = models.OneToOneField(UserAuthModel)
    site_web = models.URLField(blank=True)
    avatar = models.ImageField(null=False, blank=True, upload_to="avatars/")
    signature = models.TextField(blank=True)
    inscrit_newsletter = models.BooleanField(default=False)

    def __str__(self):
        return "Profile de {}".format(self.user)
