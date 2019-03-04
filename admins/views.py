from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse
from admins.models import Utilisateur
from .forms import UtilisateurForm

# Create your views here.

def liste_utilisateur(resquest, message = ''):
    user = Utilisateur.objects.all()
    return render(resquest, 'Admin/liste_utilisateurs.html', locals())


def add_utilisateur(resquest):
    form_user = UtilisateurForm(resquest.POST or None)

    if resquest.method == 'POST':
        if form_user.is_valid():
            nomUser = resquest.POST.get('nom_utilisateur')
            mdpUser = resquest.POST.get('mdp_utilisateur')
            CmdpUser = resquest.POST.get('comfirmMdpUtilisateur')
            actifUser = resquest.POST.get('actif_utilisateur')
            estAdmin = resquest.POST.get('est_admin')

            if mdpUser == CmdpUser:
                form_user.save()
                form_user = UtilisateurForm(None)

                return redirect(liste_utilisateur, message='success_add')
            else:
                form_user = UtilisateurForm(resquest.POST)
                error = 'La Confirmation du Mot de Passe Incorrecte'
                return render(resquest, 'Admin/add_utilisateur.html', locals())
    else:
        return render(resquest, 'Admin/add_utilisateur.html', locals())

def edit_utilisateur(resquest, user_id):
    user = Utilisateur.objects.get(id=user_id)
    if resquest.method == 'POST':

        user.nom_utilisateur    = resquest.POST.get('nom_utilisateur')
        user.est_admin          = resquest.POST.get('est_admin')
        user.actif_utilisateur  = resquest.POST.get('actif_utilisateur')
        user.save()

        return redirect(liste_utilisateur, message='success_edit')
    else:
        donnees = {
            'nom_utilisateur': user.nom_utilisateur,
            'actif_utilisateur': user.actif_utilisateur,
            'est_admin': user.est_admin
        }
        form_user = UtilisateurForm(donnees)

        return render(resquest, 'Admin/edit_utilisateur.html', locals())


