from django.http import HttpResponse, Http404
from datetime import datetime
from django.shortcuts import render, redirect
from django.shortcuts import render

# Create your views here.

def home(resquest):
    return render(resquest,'base.html')

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

def loc_home(resquest):
    return render(resquest, 'm-location/doc-loc-home.html')

def pai_home(resquest):
    return render(resquest, 'm-paie/doc-pai-home.html')