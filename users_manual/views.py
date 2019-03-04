from _ast import mod

from django.http import HttpResponse, Http404
from datetime import datetime
from django.utils.datastructures import MultiValueDictKeyError
from django.utils import timezone
from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import ModuleForm, TitreForm, ParagrapheForm
from .models import Module, Titre, SousTitre, Paragraphe, Image

# Create your views here.

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
    paragraphe_image = []
    GLOBAL_DETAILS_TITLE = []

    for subtitle in s_titre:
        paragraphe_by_subtitle.append([subtitle.intitule,Paragraphe.objects.filter(soustitre=subtitle), subtitle.id])

    for elt in paragraphe_by_subtitle:
        for e in elt[1]:
            img = Image.objects.filter(paragraphe=e)
            if img:
                GLOBAL_DETAILS_TITLE.append([elt[0], [e, [img]],elt[2]])
            else:
                GLOBAL_DETAILS_TITLE.append([elt[0], [e, []],elt[2]])

    context = {
        'title':title,
        'next_title':next_title,
        'prev_title':prev_title,
        's_titre':s_titre,
        'GLOBAL_DETAILS_TITLE':GLOBAL_DETAILS_TITLE
    }
    return render(resquest, 'details-of-title.html', context)

def add_paragraph(resquest, id_sous_titre = None):
    sous_titre = SousTitre.objects.get(id = id_sous_titre)
    form_paragrah = ParagrapheForm(resquest.POST or None)
    if resquest.method == 'POST':
        if form_paragrah.is_valid():
            form_paragrah.soustitre = sous_titre
            form_paragrah.save()
    return render(resquest, 'add-paragraphe.html', locals())

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

def add_titre(resquest, id_module, err=''):
    try:
        module = Module.objects.get(id=id_module)
        form = TitreForm(resquest.POST or None)
        if resquest.method == 'POST':
            CODE = resquest.POST['code']
            INTITULE = resquest.POST['intitule']
            POSITION = resquest.POST['position']
            DATE_CREATION = timezone.now()
            DATE_EDITION = timezone.now()
            titre = Titre(
                code=CODE,
                intitule=INTITULE,
                position=POSITION,
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

def edit_titre(resquest, id_titre):
    try:
        title = Titre.objects.get(id=id_titre)
        form = TitreForm(instance=title)
        return render(resquest, 'titres/edit-titre.html', locals())
    except Titre.DoesNotExist:
        title = None
#Module SCOLARITE

def home_sco(resquest):
    return render(resquest, 'm-scolarite/home-doc-scolarity.html')

def sco_conf(resquest):
    return render(resquest, 'm-scolarite/doc-sco-config.html')

def sco_intro(resquest):
    return render(resquest, 'm-scolarite/doc-sco-intro.html')

def sco_gest_etudiant(resquest):
    return render(resquest, 'm-scolarite/doc-sco-gest-etd.html')

def sco_gest_paiement(resquest):
    return render(resquest, 'm-scolarite/doc-sco-gest-pai.html')

def sco_gest_bourse_rec(resquest):
    return render(resquest, 'm-scolarite/doc-sco-bourse-rec.html')

def sco_gest_exm_nat(resquest):
    return render(resquest, 'm-scolarite/doc-sco-exm-nat.html')

def sco_gest_moratoire(resquest):
    return render(resquest, 'm-scolarite/doc-sco-moratoire.html')

def sco_gest_etat(resquest):
    return render(resquest, 'm-scolarite/doc-sco-etats.html')

def sco_gest_carte(resquest):
    return render(resquest, 'm-scolarite/doc-sco-carte.html')

#Module ADMISSION

def adm_home(resquest):
    return render(resquest, 'm-admission/doc-adm-home.html')

def adm_intro(resquest):
    return render(resquest, 'm-admission/doc-adm-intro.html')

def adm_config(resquest):
    return render(resquest, 'm-admission/doc-adm-config.html')

def adm_online(resquest):
    return render(resquest, 'm-admission/doc-adm-online.html')

def adm_inscand(resquest):
    return render(resquest, 'm-admission/doc-adm-insc-cand.html')

def adm_val(resquest):
    return render(resquest, 'm-admission/doc-adm-validation.html')

def adm_note(resquest):
    return render(resquest, 'm-admission/doc-adm-note.html')

def adm_valcand(resquest):
    return render(resquest, 'm-admission/doc-adm-val-adm.html')

#Module LOCATION

def loc_home(resquest):
    return render(resquest, 'm-location/doc-loc-home.html')

def loc_intro(resquest):
    return render(resquest, 'm-location/doc-loc-intro.html')

def loc_config(resquest):
    return render(resquest, 'm-location/doc-loc-config.html')

def loc_locataire(resquest):
    return render(resquest, 'm-location/doc-loc-locataire.html')

def loc_contrat(resquest):
    return render(resquest, 'm-location/doc-loc-contrat.html')

def loc_paiement(resquest):
    return render(resquest, 'm-location/doc-loc-paiement.html')

#Module PAIE

def pai_home(resquest):
    return render(resquest, 'm-paie/doc-pai-home.html')