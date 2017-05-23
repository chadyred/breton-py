#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

# Instance permettant d'enregistrer nos filtres
register = template.Library()

@register.filter(is_safe=True)
def citation(texte):
	texte = "&laquo; {} &raquo;".format(escape(texte));

	return mark_safe(texte);

@register.filter
def smart_truncate(texte, nbCaractere):
	"""Troncature du texte au X caractere, le mot tronque est exclus"""

	try:
		nbCaractere = int(nbCaractere)
	except ValueError:
		return texte

	if nbCaractere >= len(texte):
		return texte

		# L'ajout d'un caractère permet de savoir si on est à la fin d'un mot (un espace) ou en plein milieu (un caractère)
	texteTruncate = texte[:nbCaractere + 1]

	# Deux cas: on a un espace a la fin on ne pas le mot, sinon on prend tout les mots en retirant le dernier
	if texte[-1:] == " ":
		texteTruncate = texteTruncate[0:-1]
	else:
		# Cela signifie que l'on est au milieu d'un mot, on va alors jusqu'a l'avant dernier mot
		texteTruncate = texteTruncate.split(' ')[:-1]
		texteTruncate = ' '.join(texteTruncate)

	return texteTruncate + '...'
