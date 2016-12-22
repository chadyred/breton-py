# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Personne(models.Model):
    sexe = models.CharField(max_length=10, default="male")
    nom = models.CharField(max_length=31)
    prenom = models.CharField(max_length=31, default="Unknow")

    class Meta:
        abstract = True

class Eleve(Personne):
    moyenne = models.IntegerField(default=10)

    def __str__(self):
        return "Élève {0} ({1}/20 de moyenne)".format(self.nom, self.moyenne)

class Cours(models.Model):
	"""Cours"""

	eleves = models.ManyToManyField(Eleve)
	nom = models.CharField(max_length=31)

	def __str__(self):
		return self.nom

class Surveillant(Eleve):
    """Ici on note les surveillant, et ce sous des élève malfammé :)"""
    rang = models.IntegerField(default=1)

class SurveillantProxy(Surveillant):
    """On bénéficie de méthode supplémentaire, on peut accéder aux donnée du parent sans pour autant altérer le modèle."""
    coup_de_fouet = 0

    class Meta:
        """On change les information sur les classe hérité"""
        proxy = True
        ordering = ['rang']

    def coupDeFouet(self):
        """Coup de fouet selon le rang"""

        if self.rang == 1:
            self.coup_de_fouet = 2
        elif self.rang == 2:
            self.coup_de_fouet = 3

        return self.coup_de_fouet