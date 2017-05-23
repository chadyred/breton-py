from django import forms
from blog.models import Categorie, Article
from oauth.models import Profile

class ArticleForm(forms.Form):
    titre = forms.CharField(max_length=100)
    contenu = forms.CharField(required=True,widget=forms.Textarea)
    image = forms.ImageField(required=False)
    auteur = forms.ModelChoiceField(queryset=Profile.objects.all())
    categorie = forms.ModelChoiceField(queryset=Categorie.objects.all())

class ArticleModelForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"
