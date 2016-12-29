from datetime import datetime

def dateActuelle(request):
	"""Ajout d ela date dans tout nos template"""
	date_actuelle = datetime.now()

	return {'date_actuelle' : date_actuelle}