from django import forms
from django.forms import ModelForm, Textarea, TextInput, NumberInput, ImageField
from .models import Paragraphe, Module, Titre

class ModuleForm(ModelForm):
    class Meta:
        model = Module
        fields = ['code', 'intitule', 'position', 'photo', 'date_creation', 'date_edition']
        widgets = {
            'code'      : TextInput(attrs={'class': 'blue-grey-text text-darken-4'}),
            'intitule'  : TextInput(attrs={'class': 'blue-grey-text text-darken-4'}),
            'position'  : NumberInput(attrs={'class': 'blue-grey-text text-darken-4'})
        }

class TitreForm(ModuleForm):
    class Meta:
        model = Titre
        fields = ['code', 'intitule', 'position', 'date_creation', 'date_edition']
        widgets = {
            'code': TextInput(attrs={'class': 'blue-grey-text text-darken-4'}),
            'intitule': TextInput(attrs={'class': 'blue-grey-text text-darken-4'}),
            'position': NumberInput(attrs={'class': 'blue-grey-text text-darken-4'})
        }

class ParagrapheForm(ModelForm):

    class Meta:
        model = Paragraphe
        fields = '__all__'
        widgets = {
            'contenu': Textarea(attrs={'class':'materialize-textarea'})
        }