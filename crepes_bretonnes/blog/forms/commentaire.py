from django import forms
from oauth.models import Profile

class CommentaireForm(forms.Form):
    titre = forms.CharField(max_length=100)
    contenu = forms.CharField(required=True,widget=forms.Textarea)