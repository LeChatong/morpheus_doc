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


def adm_home(resquest):
    return render(resquest, 'm-admission/doc-adm-home.html')

def adm_intro(resquest):
    return render(resquest, 'm-admission/doc-adm-intro.html')

def adm_config(resquest):
    return render(resquest, 'm-admission/doc-adm-config.html')

def loc_home(resquest):
    return render(resquest, 'm-location/doc-loc-home.html')

def pai_home(resquest):
    return render(resquest, 'm-paie/doc-pai-home.html')