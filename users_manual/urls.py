from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('Acceuil', views.home, name='morpheus_doc'),
    path('doc-sco.html', views.home_sco, name='sco_accueil'),
    path('doc-sco-config-pension.html', views.sco_conf, name='sco_config_pension'),
    path('doc-sco-intro.html', views.sco_intro, name='sco_intro'),
    path('doc-sco-etd.html', views.sco_gest_etudiant, name='sco_gest_etud'),
    path('doc-sco-paie.html', views.sco_gest_paiement, name='sco_gest_paie'),
    path('doc-sco-bourserec.html', views.sco_gest_bourse_rec, name='sco_gest_bourse_rec'),
    path('doc-sco-exmnat.html', views.sco_gest_exm_nat, name='sco_gest_exm_nat'),

    path('doc-adm.html',views.adm_home,name='adm_acceuil'),
    path('doc-adm-intro.html',views.adm_intro,name='adm_intro'),
    path('doc-adm-config.html',views.adm_config,name='adm_config'),
    path('doc-adm-online.html',views.adm_online,name='adm_online'),
    path('doc-adm-insc-cand.html',views.adm_inscand,name='adm_inscand'),
    path('doc-adm-validation.html',views.adm_val,name='adm_val'),
    path('doc-adm-note.html',views.adm_note,name='adm_note'),
    path('doc-adm-val_cand.html',views.adm_valcand,name='adm_val_cand'),

    path('doc-loc.html',views.loc_home,name='loc_acceuil'),
    path('doc-pai.html',views.pai_home,name='pai_acceuil')
]