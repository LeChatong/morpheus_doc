from django import forms
from froala_editor.widgets import FroalaEditor
from tinymce import TinyMCE
from django.forms import ModelForm, Textarea, TextInput, NumberInput, ImageField
from .models import Paragraphe, Module, Titre, SousTitre

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
    description = forms.CharField(widget=TinyMCE(), empty_value=True)
    class Meta:
        model = Titre
        fields = ['code', 'intitule', 'description', 'position', 'date_creation', 'date_edition']
        widgets = {
            'code': TextInput(attrs={'class': 'blue-grey-text text-darken-4'}),
            'intitule': TextInput(attrs={'class': 'blue-grey-text text-darken-4'}),
            'position': NumberInput(attrs={'class': 'blue-grey-text text-darken-4'})
        }

class SousTitreForm(ModuleForm):

    class Meta:
        model = SousTitre
        fields = ['intitule', 'position', 'date_creation', 'date_edition']
        widgets = {
            'intitule': TextInput(attrs={'class': 'blue-grey-text text-darken-4'}),
            'position': NumberInput(attrs={'class': 'blue-grey-text text-darken-4'})
        }

class ParagrapheForm(ModuleForm):
    contenu = forms.CharField(widget=TinyMCE())
    img = forms.ImageField(allow_empty_file=True,required=False)
    intitule_img = forms.CharField(empty_value=True, required=False)
    class Meta:
        model = Paragraphe
        fields = ['contenu', 'img', 'intitule_img', 'date_creation', 'date_edition']

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
