from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('Acceuil', views.home, name='morpheus_doc'),
    path('doc-sco.html', views.home_sco, name='sco_accueil'),
    path('doc-sco-config-pension.html', views.sco_conf, name='sco_config_pension'),
    path('doc-sco-intro.html', views.sco_intro, name='sco_intro'),
    path('doc-sco-etd.html', views.sco_gest_etudiant, name='sco_gest_etud'),

    path('doc-adm.html',views.adm_home,name='adm_acceuil'),
    path('doc-adm-intro.html',views.adm_intro,name='adm_intro'),
    path('doc-adm-config.html',views.adm_config,name='adm_config'),

    path('doc-loc.html',views.loc_home,name='loc_acceuil'),
    path('doc-pai.html',views.pai_home,name='pai_acceuil')
]