from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [

    path('Acceuil', views.home, name='morpheus_doc'),
    path('', views.home, name='morpheus_doc'),
    path('add/module/', views.add_module, name='add-module'),
    path('add/module/<str:err>/', views.add_module),
    path('edit/module/<int:id>/', views.edit_module, name='edit-module'),
    path('delete/module/<int:id>/', views.delete_module, name='delete-module'),
    path('module/<str:mod>/<int:id_module>/', views.home_module, name='home-module'),
    path('titre/<int:id_titre>/', views.detail_of_title, name='detail-titre'),
    path('add/titre/<int:id_module>/', views.add_titre, name='add-titre'),
    path('add/titre/<int:id_module>/<str:err>/', views.add_titre),
    path('edit/titre/<int:id_titre>/', views.edit_titre, name='edit-titre'),
    path('add/paragraph/<int:id_sous_titre>/', views.add_paragraph, name='add_paragraph'),



    path('doc-sco.html', views.home_sco, name='sco_accueil'),
    path('doc-sco-config-pension.html', views.sco_conf, name='sco_config_pension'),
    path('doc-sco-intro.html', views.sco_intro, name='sco_intro'),
    path('doc-sco-etd.html', views.sco_gest_etudiant, name='sco_gest_etud'),
    path('doc-sco-paie.html', views.sco_gest_paiement, name='sco_gest_paie'),
    path('doc-sco-bourserec.html', views.sco_gest_bourse_rec, name='sco_gest_bourse_rec'),
    path('doc-sco-exmnat.html', views.sco_gest_exm_nat, name='sco_gest_exm_nat'),
    path('doc-sco-moratoire.html', views.sco_gest_moratoire, name='sco_gest_moratoire'),
    path('doc-sco-etat.html', views.sco_gest_etat, name='sco_gest_etat'),
    path('doc-sco-cartes-etd.html', views.sco_gest_carte, name='sco_gest_cartes'),

    path('doc-adm.html',views.adm_home,name='adm_acceuil'),
    path('doc-adm-intro.html',views.adm_intro,name='adm_intro'),
    path('doc-adm-config.html',views.adm_config,name='adm_config'),
    path('doc-adm-online.html',views.adm_online,name='adm_online'),
    path('doc-adm-insc-cand.html',views.adm_inscand,name='adm_inscand'),
    path('doc-adm-validation.html',views.adm_val,name='adm_val'),
    path('doc-adm-note.html',views.adm_note,name='adm_note'),
    path('doc-adm-val_cand.html',views.adm_valcand,name='adm_val_cand'),

    path('doc-loc.html',views.loc_home,name='loc_acceuil'),
    path('doc-loc-intro.html',views.loc_intro,name='loc_intro'),
    path('doc-loc-config.html',views.loc_config,name='loc_config'),
    path('doc-loc-locataire.html',views.loc_locataire,name='loc_locataire'),
    path('doc-loc-contrat.html',views.loc_contrat,name='loc_contrat'),
    path('doc-loc-paiement.html',views.loc_paiement,name='loc_paiement'),

    path('doc-pai.html',views.pai_home,name='pai_acceuil')
]