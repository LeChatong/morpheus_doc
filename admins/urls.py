from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('user/list', views.liste_utilisateur, name='liste-utilisateurs'),
    path('user/list/<str:message>/', views.liste_utilisateur),
    path('user/add', views.add_utilisateur, name='add_utilisateur'),
    path('user/edit/<int:user_id>/', views.edit_utilisateur, name='edit_user')
]