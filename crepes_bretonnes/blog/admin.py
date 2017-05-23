#-*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin

from .models import Article, Commentaire, Categorie, Crepe, Ingredient, CrepeIngredient
# Register your models here.
# admin.site.register(Article)
# admin.site.register(Crepe)
admin.site.register(Commentaire)
admin.site.register(Categorie)
admin.site.register(Ingredient)
admin.site.register(CrepeIngredient)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("titre", "auteur","contenu", "date")
    list_filter = ("titre",)
    ordering = ("auteur", "titre")
    date_hierarchy = "date"
    search_fields = ("titre",)

class CrepeAdmin(admin.ModelAdmin):
    list_display = ("nom", "crepe_ingredients")
    list_filter = ("nom",)
    ordering = ("nom",)
    search_fields = ("nom",)

    def crepe_ingredients(self, crepe):
      """Show all format ingredient"""

      return ' '.join([str(elt) for elt in crepe.crepeingredient_set.all()])

    crepe_ingredients.short_description = "Liste des ingrédients"

admin.site.register(Article, ArticleAdmin)
admin.site.register(Crepe, CrepeAdmin)