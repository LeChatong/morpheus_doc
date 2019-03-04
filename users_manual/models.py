from django.db import models
from django.utils import timezone

# Create your models here.

class Module(models.Model):
    code            = models.CharField(max_length=25)
    intitule        = models.CharField(max_length=50)
    date_creation   = models.DateTimeField(default=timezone.now)
    date_edition    = models.DateTimeField(default=timezone.now)
    photo           = models.ImageField(upload_to="photos/")
    position        = models.IntegerField(default=0)
    class Meta:
        verbose_name    = 'module'
        ordering        = ['position']
    def __str__(self):
        return self.code

class Titre(models.Model):
    code            = models.CharField(max_length=25)
    intitule        = models.CharField(max_length=100)
    date_creation   = models.DateTimeField(default=timezone.now)
    date_edition    = models.DateTimeField(default=timezone.now)
    position        = models.IntegerField(default=0)
    module          = models.ForeignKey(Module, on_delete=models.PROTECT)
    class Meta:
        verbose_name    = 'titre'
        ordering        = ['position']
    def __str__(self):
        return self.intitule

class SousTitre(models.Model):
    intitule        = models.CharField(max_length=100)
    position        = models.IntegerField(default=0)
    titre           = models.ForeignKey(Titre, on_delete=models.PROTECT)
    date_creation   = models.DateTimeField(default=timezone.now)
    date_edition    = models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name    = 'sous_titre'
        ordering        = ['position']
    def __str__(self):
        return self.intitule

class Paragraphe(models.Model):
    contenu         = models.TextField()
    soustitre       = models.ForeignKey(SousTitre, on_delete=models.PROTECT)
    date_creation   = models.DateTimeField(default=timezone.now)
    date_edition    = models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name    = 'paragraphe'
        ordering        = ['date_creation']

class Image(models.Model):
    intitule        = models.CharField(max_length=100)
    photo           = models.ImageField(upload_to="photos/")
    paragraphe      = models.ForeignKey(Paragraphe, on_delete=models.PROTECT)
    date_creation   = models.DateTimeField(default=timezone.now)
    date_edition    = models.DateTimeField(default=timezone.now)
    class Meta:
        verbose_name    = 'image'
        ordering        = ['date_creation']
    def __str__(self):
        return self.intitule