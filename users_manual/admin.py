from django.contrib import admin
from django.utils.text import Truncator
from .models import Module, Titre, SousTitre, Paragraphe


class ModuleAdmin(admin.ModelAdmin):
    list_display = ('code', 'intitule', 'photo', 'position', 'date_creation', 'date_edition')
    list_filter = ('code', 'intitule')
    date_hierarchy = 'date_creation'
    search_fields = ('code', 'intitule')
    ordering = ('position',)

class TitreAdmin(admin.ModelAdmin):
    list_display = ('details','mod', 'position', 'description', 'date_creation', 'date_edition')
    list_filter = ('code',)
    date_hierarchy = 'date_creation'
    search_fields = ('code', 'intitule')
    ordering = ('position',)
    list_per_page = 25
    fieldsets = (
        ('Général', {
            'classes': ['wide','extrapretty' ],
            'fields': ('code', 'intitule', 'module')
        }),
        ('Dates', {
            'classes': ['extrapretty', ],
            'description': 'Ici sont présent les dates de création et de mise à jour d\'un Titre' ,
            'fields': ('date_creation', 'date_edition')
        }),
    )
    def mod(self, obj):
        return obj.module.intitule
    def details(self, obj):
        return ("%s / %s" % (obj.code, obj.intitule)).upper()

    details.short_description = 'Détails'

class SousTitreAdmin(admin.ModelAdmin):
    list_display = ('intitule', 'position', 'date_creation', 'date_edition')
    list_filter = ('intitule',)
    date_hierarchy = 'date_creation'
    list_per_page = 25
    search_fields = ('intitule',)
    ordering = ('position',)

class ParagrapheAdmin(admin.ModelAdmin):
    list_display = ('details_paragraphe','contenu_trunc', 'date_creation', 'date_edition')
    date_hierarchy = 'date_creation'
    list_per_page = 25
    ordering = ('date_creation',)
    def contenu_trunc(self, obj):
        return ("%s" % Truncator((obj.contenu)).chars(40, truncate='...'))
    def details_paragraphe(self, obj):
        return ("%s" % (obj.soustitre.intitule))

        details_paragraphe.short_description = 'Détails'
    contenu_trunc.short_description = 'Contenu'

# Register your models here.

admin.site.register(Module, ModuleAdmin)
admin.site.register(Titre, TitreAdmin)
admin.site.register(SousTitre, SousTitreAdmin)
admin.site.register(Paragraphe, ParagrapheAdmin)
