from django import forms
from .models import Categorie, User, Article

class ArticleForm(forms.Form):
    titre = forms.CharField(max_length=100)
    contenu = forms.CharField(required=True,widget=forms.Textarea)
    auteur = forms.ModelChoiceField(queryset=User.objects.all())
    categorie = forms.ModelChoiceField(queryset=Categorie.objects.all())

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
