# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Eleve(models.Model):
	"""Eleve"""

	nom = models.CharField(max_length=31)
	moyenne = models.IntegerField(default=10)

	def __str__(self):
		return "Élève {0} ({1}/20 de moyenne)".format(self.nom, self.moyenne)

class Cours(models.Model):
	"""Cours"""

	eleves = models.ManyToManyField(Eleve)
	nom = models.CharField(max_length=31)

	def __str__(self):
		return self.nom