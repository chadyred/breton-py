# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.utils.translation import ugettext as _


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

def test_i18n(request):
	nb_chat = 2
	# Translators: cat behaviour
	caracter = _("drole")
	nom_chien = "Lololilo"
	chien = _("Ton magnifique chien s'appel %(nom_chien)s.") % {'nom_chien': nom_chien}
	hello = _("Monde")
	ip = _("Votre ip est %(ip)s") % {'ip' : request.META["REMOTE_ADDR"]}
	petit = _("Je suis tout petit.")

	chat = ungettext(
			"Vous avez %(nb_chat)s chat %(caracter)s",
			"Vous avez %(nb_chat)s chats %(caracter)ss",
			nb_chat) % {"nb_chat" : nb_chat, "caracter": caracter}
	crocodile = pgettext("Crocodile de compagnie dans la famille pirate","sac-à-main")
	sac = pgettext("Sac pour transporter des affaires","sac-à-main")

	action = _("Viens %(animal)s, mais avant %s(suj) doit prendre mon %(objet)s") %
			{
				'suj' : _('je')
				'objet' : sac,
				'animal' : crocodile
			}

	return render(request, 'app/testi18n.html', locals())