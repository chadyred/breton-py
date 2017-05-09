#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User as UserAuthModel

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(UserAuthModel)
    site_web = models.URLField(blank=True)
    avatar = models.ImageField(null=False, blank=True, upload_to="avatars/")
    signature = models.TextField(blank=True)
    inscrit_newsletter = models.BooleanField(default=False)

    def __str__(self):
        return "Profile de {}".format(self.user)

# TODO : REMOVE IT AND EXTENDS THE EXISTANT MODEL OF DJANGO
class User(models.Model):
    username = models.TextField(max_length=255)
    # On fera eniteArticle.user_tag afin d'avoir les utilisateur qui ont taggé cette article
    articlesTag = models.ManyToManyField('blog.Article', through='blog.UserTagArticle', related_name="user_tag")

    def __str__(self):
        return self.username
