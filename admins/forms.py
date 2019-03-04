from django import forms
from django.forms import ModelForm, TextInput, PasswordInput, CheckboxInput
from .models import Utilisateur



class UtilisateurForm(ModelForm):

    class Meta:
        model = Utilisateur
        fields = ["nom_utilisateur", "mdp_utilisateur", "actif_utilisateur", "est_admin"]
        widgets = {
            'nom_utilisateur': TextInput(attrs={'class': 'blue-text text-darken-4'}),
            'mdp_utilisateur': PasswordInput(attrs={'class': 'blue-text text-darken-4'}),
            'confirmMdpUtilisateur': PasswordInput(attrs={'class': 'blue-text text-darken-4'}),
            'actif_utilisateur' : CheckboxInput(),
            'est_admin': CheckboxInput()
        }