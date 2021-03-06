#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from oauth.models import Profile

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver, Signal # decorateur : permet de modifier la fonction

from django.utils.translation import ugettext_lazy as _
from datetime import datetime


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
    date = models.DateTimeField( auto_now=True, auto_now_add=False, verbose_name=_("Date de parution") )
    image = models.ImageField(upload_to="article/", null=True)
    nbVue = models.IntegerField(default=0)

    categorie = models.ForeignKey('Categorie')
    auteur = models.ForeignKey(Profile)
    commentaires = GenericRelation('blog.Commentaire')

    def is_recent(self):
        """Les 30 day"""
        dateDiff = datetime.now() - self.date #create a timedelta

        return dateDiff.days < 30

    def __str__(self):
        """
        Article de notre super blog !! intitulé
        """
        return self.titre
    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")
        permissions = (
                ("article_add_comment","Commenter un article"),
                ("article_add_like","Like un article")
            )

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

class Tag(models.Model):
    libelle = models.TextField(max_length=100)
    article = models.ManyToManyField(Article,through="UserTagArticle")

    def __str__(self):
        return "#" + self.libelle

class UserTagArticle(models.Model):
    user = models.ForeignKey(Profile)
    tag = models.ForeignKey(Tag)
    article = models.ForeignKey(Article)

    def __str__(self):
        return "{0} à tagger : {1} sur l'article {2}".format(self.user, self.tag, self.article)

class Commentaire(models.Model):
    """Commentaire généric (pouvant être associé à plusieurs modèle)"""

    titre = models.CharField(max_length=100, null=False)
    contenu = models.TextField(null=False)

    user = models.ForeignKey(Profile)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')

    def __str__(self):
        return "Commentaire {} sur l'article {} de {}".format(self.titre, self.article, self.user)

class Page(models.Model):
    url = models.URLField()
    nb_visit = models.IntegerField(default=1)

    def __str__(self, page):
        return self.url;
