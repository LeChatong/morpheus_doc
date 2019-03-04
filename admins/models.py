from django.db import models
from django.utils import timezone

# Create your models here.

class Utilisateur(models.Model):
    nom_utilisateur = models.CharField(verbose_name="Compte",max_length=45)
    mdp_utilisateur = models.CharField(verbose_name="Mot de Passe",max_length=45)
    actif_utilisateur = models.BooleanField(verbose_name="Actif")
    est_admin = models.BooleanField(verbose_name="Administrateur")
    date_sauvegarde = models.DateTimeField(default=timezone.now, verbose_name="Date de Sauvegarde")
    date_maj = models.DateTimeField(default=timezone.now, verbose_name="Date de Mise à Jour")

    class Meta:
        verbose_name = "Utilisateur"
        ordering = ['date_sauvegarde']

    def __str__(self):
        return self.nom_utilisateur
