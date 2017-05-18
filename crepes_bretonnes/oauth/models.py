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
    articlesTag = models.ManyToManyField('blog.Article', through='blog.UserTagArticle', related_name="user_tag")

    def __str__(self):
        return "Profile de {}".format(self.user)
