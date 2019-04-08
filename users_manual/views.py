from _ast import mod

from django.http import HttpResponse, Http404
from datetime import datetime
from django.utils.datastructures import MultiValueDictKeyError
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse
from .forms import ModuleForm, TitreForm, SousTitreForm, ParagrapheForm, ConnexionForm
from .models import Module, Titre, SousTitre, Paragraphe
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
def connexion(resquest):
    form = ConnexionForm(resquest.POST)
    error = False

    if resquest.method == "POST":
        form = ConnexionForm(resquest.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(resquest, user)
                modules = Module.objects.all()
                return render(resquest, 'base.html', locals())
            else:
                error = True
    else:
        form = ConnexionForm()
    return render(resquest, 'connexion.html',locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))

def home(resquest):
    modules = Module.objects.all()
    return render(resquest,'base.html',locals())

def home_module(resquest, mod ='', id_module = None):
    mod = Module.objects.get(id=id_module)
    titres = Titre.objects.filter(module=mod)
    return render(resquest, 'home-module.html', locals())

def detail_of_title(resquest, id_titre = None):
    title = Titre.objects.get(id=id_titre)
    #n_pos = title.position+1
    #p_pos = title.position - 1
    try:
        next_title = Titre.objects.get(position=(title.position + 1), module=title.module)
    except Titre.DoesNotExist:
        next_title = None

    try:
        prev_title = Titre.objects.get(position=(title.position - 1), module=title.module)
    except Titre.DoesNotExist:
        prev_title = None

    s_titre = SousTitre.objects.filter(titre=title)
    paragraphe_by_subtitle = []
    #paragraphe_image = []
    #GLOBAL_DETAILS_TITLE = []

    for subtitle in s_titre:
        paragraphe_by_subtitle.append([subtitle.intitule,Paragraphe.objects.filter(soustitre=subtitle), subtitle.id])

    #for elt in paragraphe_by_subtitle:
    #    for e in elt[1]:
    #        img = Image.objects.filter(paragraphe=e)
    #        if img:
    #            GLOBAL_DETAILS_TITLE.append([elt[0], [e, [img]],elt[2]])
    #        else:
    #            GLOBAL_DETAILS_TITLE.append([elt[0], [e, []],elt[2]])

    context = {
        'title':title,
        'next_title':next_title,
        'prev_title':prev_title,
        's_titre':s_titre,
        'paragraphe_by_subtitle': paragraphe_by_subtitle
        #'GLOBAL_DETAILS_TITLE':GLOBAL_DETAILS_TITLE
    }
    return render(resquest, 'details-of-title.html', context)

@login_required()
def add_paragraph(resquest, id_sous_titre):
    sous_titre = SousTitre.objects.get(id = id_sous_titre)
    form = ParagrapheForm(resquest.POST or None)
    if resquest.method == 'POST':
        CONTENU = resquest.POST['contenu']
        try:
            IMG = resquest.FILES['img']
        except MultiValueDictKeyError:
            IMG = None
        INTITULE_IMG = resquest.POST['intitule_img']
        DATE_CREATION = timezone.now()
        DATE_EDITION = timezone.now()

        paragraphe = Paragraphe(
            contenu= CONTENU,
            img= IMG,
            intitule_img= INTITULE_IMG,
            date_creation= DATE_CREATION,
            date_edition= DATE_EDITION,
            soustitre= sous_titre
        )
        paragraphe.save()
        return redirect(detail_of_title,id_titre =sous_titre.titre.id)
    else:
        return render(resquest, 'add-paragraphe.html', locals())

@login_required()
def add_module(resquest, err=''):
    form = ModuleForm(resquest.POST or None)
    if resquest.method == 'POST':
        #if form.is_valid():
        CODE            = resquest.POST['code']
        INTITULE        = resquest.POST['intitule']
        POSITION        = resquest.POST['position']
        try:
            PHOTO = resquest.FILES['photo']
        except MultiValueDictKeyError:
            PHOTO = None
        DATE_CREATION   = timezone.now()
        DATE_EDITION    = timezone.now()
        module = Module(
            code= CODE,
            intitule= INTITULE,
            position= POSITION,
            photo= PHOTO,
            date_creation= DATE_CREATION,
            date_edition= DATE_EDITION
        )
        try:
            mod = Module.objects.get(code=module.code)
        except Module.DoesNotExist:
            mod = None

        if mod:
            err = 'err1'
            return render(resquest, 'add-module.html', locals())
        else:
            module.save()
            return redirect(home)
        #else:
        #    return render(resquest, 'add-module.html', locals())
    else:
        return render(resquest, 'add-module.html', locals())

@login_required()
def edit_module(resquest, id):
    try:
        module = Module.objects.get(id=id)
    except Module.DoesNotExist:
        module

    if resquest.method == 'POST':
        CODE = resquest.POST['code']
        INTITULE = resquest.POST['intitule']
        POSITION = resquest.POST['position']
        try:
            PHOTO = resquest.FILES['photo']
        except MultiValueDictKeyError:
            PHOTO = None

        DATE_EDITION = timezone.now()

        module.code = CODE
        module.intitule = INTITULE
        module.position = POSITION
        module.photo = PHOTO
        module.date_edition =DATE_EDITION
        module.save()
        return redirect(home)
    else:
        form = ModuleForm(instance=module)
        return render(resquest, 'modules/edit-module.html', locals())

@login_required()
def delete_module(resquest, id):
    try:
        module = Module.objects.get(id=id)
    except Module.DoesNotExist:
        module
    if resquest.method == 'POST':
        module.delete()
        return redirect(home)
    else:
        return render(resquest, 'modules/delete-module.html', locals())

@login_required()
def add_titre(resquest, id_module, err=''):
    try:
        module = Module.objects.get(id=id_module)
        form = TitreForm(resquest.POST or None)
        if resquest.method == 'POST':
            CODE = resquest.POST['code']
            INTITULE = resquest.POST['intitule']
            POSITION = resquest.POST['position']
            DESCRIPTION = resquest.POST['description']
            DATE_CREATION = timezone.now()
            DATE_EDITION = timezone.now()
            titre = Titre(
                code=CODE,
                intitule=INTITULE,
                position=POSITION,
                description=DESCRIPTION,
                module=module,
                date_creation=DATE_CREATION,
                date_edition=DATE_EDITION
            )
            try:
                title = Titre.objects.get(code=titre.code)
            except Titre.DoesNotExist:
                title = None

            if title:
                err ='error_code'
                return render(resquest, 'titres/add-titre.html', locals())
            else:
                titre.save()
                return redirect(home_module, mod = module.code, id_module = module.id)
        else:
            return render(resquest, 'titres/add-titre.html', locals())

    except Module.DoesNotExist:
        module

@login_required()
def edit_titre(resquest, id_titre):
    try:
        title = Titre.objects.get(id=id_titre)


        if resquest.method == 'POST':
            CODE = resquest.POST['code']
            INTITULE = resquest.POST['intitule']
            DESCRIPTION = resquest.POST['description']
            POSITION = resquest.POST['position']
            DATE_EDITION = timezone.now()

            title.position = POSITION
            title.code = CODE
            title.intitule = INTITULE
            title.description = DESCRIPTION
            title.date_edition = DATE_EDITION
            title.save()
            return redirect(home_module, mod = title.module.code, id_module=title.module.id)
        else:
            form = TitreForm(instance=title)
            return render(resquest, 'titres/edit-titre.html', locals())

    except Titre.DoesNotExist:
        title = None

@login_required()
def delete_titre(resquest, id_titre):
    try:
        titre = Titre.objects.get(id=id_titre)
        if resquest.method == 'POST':
            code_module = titre.module.code
            id_module = titre.module.id
            titre.delete()
            return redirect(home_module, mod = code_module, id_module =id_module)
        else:
            return render(resquest, 'titres/delete-titre.html', locals())
    except Titre.DoesNotExist:
        titre

@login_required()
def add_subtitle(resquest, id_titre):
    try:
        titre = Titre.objects.get(id=id_titre)
        form = SousTitreForm(resquest.POST or None)
        if resquest.method == 'POST':
            INTITULE = resquest.POST['intitule']
            POSITION = resquest.POST['position']
            DATE_CREATION = timezone.now()
            DATE_EDITION = timezone.now()

            soustitre = SousTitre(
                intitule= INTITULE,
                position=POSITION,
                date_creation=DATE_CREATION,
                date_edition=DATE_EDITION,
                titre=titre
            )

            soustitre.save()
            return redirect(detail_of_title, id_titre=titre.id)
        else:
            return render(resquest, 'soustitres/add-subtitle.html', locals())
    except Titre.DoesNotExist:
        titre

@login_required()
def edit_subtitle(resquest, id):
    try:
        soustitre = SousTitre.objects.get(id=id)
        if resquest.method == "POST":
            INTITULE = resquest.POST['intitule']
            POSITION = resquest.POST['position']
            DATE_EDITION = timezone.now()

            soustitre.intitule = INTITULE
            soustitre.position = POSITION
            soustitre.date_edition = DATE_EDITION
            soustitre.save()
            return redirect(detail_of_title, id_titre = soustitre.titre.id)
        else:
            form = SousTitreForm(instance=soustitre)
            return render(resquest, 'soustitres/edit-subtitle.html', locals())
    except SousTitre.DoesNotExist:
        raise Http404

@login_required()
def delete_subtitle(resquest, id):
    try:
        soustitre = SousTitre.objects.get(id=id)
        ID_TITRE = soustitre.titre.id
        if resquest.method == "POST":
            soustitre.delete()
            return redirect(detail_of_title, id_titre = ID_TITRE)
        else:
            form = SousTitreForm(instance=soustitre)
            return render(resquest, 'soustitres/delete-subtitle.html', locals())
    except SousTitre.DoesNotExist:
        raise Http404

@login_required()
def delete_paragraphe(resquest, id):
    try:
        paragraphe = Paragraphe.objects.get(id=id)
        ID_TITRE = paragraphe.soustitre.titre.id
        if resquest.method == "POST":
            paragraphe.delete()
            return redirect(detail_of_title, id_titre=ID_TITRE)
        else:
            form = ParagrapheForm(instance=paragraphe)
            return render(resquest, 'paragraphe/delete-paragraphe.html', locals())
    except Paragraphe.DoesNotExist:
        Http404

@login_required()
def edit_paragraphe(resquest, id):
    try:
        paragraphe = Paragraphe.objects.get(id=id)
        ID_TITRE = paragraphe.soustitre.titre.id
        if resquest.method == "POST":
            CONTENU = resquest.POST['contenu']
            try:
                IMG = resquest.FILES['img']
            except MultiValueDictKeyError:
                IMG = None

            INTITULE_IMG = resquest.POST['intitule_img']
            DATE_EDITION = timezone.now()

            paragraphe.contenu = CONTENU
            paragraphe.img = IMG
            paragraphe.intitule_img = INTITULE_IMG
            paragraphe.date_edition = DATE_EDITION
            paragraphe.save()

            return redirect(detail_of_title, id_titre=ID_TITRE)
        else:
            form = ParagrapheForm(instance=paragraphe)
            return render(resquest, 'paragraphe/edit-paragraphe.html', locals())
    except Paragraphe.DoesNotExist:
        Http404
