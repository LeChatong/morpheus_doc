from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [

    path('Acceuil', views.home, name='morpheus_doc'),
    path('Connexion',views.connexion, name='connexion'),
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
    path('delete/titre/<int:id_titre>/', views.delete_titre, name='delete-titre'),
    path('add/subtitle/<int:id_titre>/', views.add_subtitle, name='add-soustitre'),
    path('edit/subtitle/<int:id>/', views.edit_subtitle, name='edit-soustitre'),
    path('delete/subtitle/<int:id>/', views.delete_subtitle, name='delete-soustitre'),
    path('add/paragraph/<int:id_sous_titre>/', views.add_paragraph, name='add_paragraph'),
    path('delete/paragraph/<int:id>/', views.delete_paragraphe, name='delete-paragraph'),
    path('edit/paragraph/<int:id>/', views.edit_paragraphe, name='edit-paragraph'),
    path('deconnexion', views.deconnexion, name='deconnexion'),
]