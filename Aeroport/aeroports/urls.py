from django.urls import path
from . import views, avions_views, compagnies_views, pistes_views, typesavions_views, vols_views

urlpatterns = [
    #Urls pour la partie aeroport
    path('formulaire/', views.formulaire),
    path('traitement/', views.traitement),
    path('indexaeroport/', views.index),
    path('', views.index),
    path('affiche/<int:id>/', views.affiche),
    path('update/<int:id>/', views.update),
    path('updatetraitement/<int:id>/', views.updatetraitement),
    path('delete/<int:id>/', views.delete),

    #Urls pour la partie avions
    path('indexavions/', avions_views.index),
    path('formulaireavions/', avions_views.formulaire),
    path('traitementavions/', avions_views.traitement),
    path('afficheavions/<int:id>/', avions_views.affiche),
    path('deleteavions/<int:id>/', avions_views.delete),
    path('updateavions/<int:id>/', avions_views.update),
    path('updatetraitementavions/<int:id>/', avions_views.updatetraitement),

    #Urls pour la partie compagnies
    path('indexcompagnies/', compagnies_views.index),
    path('formulairecompagnies/', compagnies_views.formulaire),
    path('traitementcompagnies/', compagnies_views.traitement),
    path('affichecompagnies/<int:id>/', compagnies_views.affiche),
    path('deletecompagnies/<int:id>/', compagnies_views.delete),
    path('updatecompagnies/<int:id>/', compagnies_views.update),
    path('updatetraitementcompagnies/<int:id>/', compagnies_views.updatetraitement),

    #Urls pour la partie pistes
    path('indexpistes/', pistes_views.index),
    path('formulairepistes/', pistes_views.formulaire),
    path('traitementpistes/', pistes_views.traitement),
    path('affichepistes/<int:id>/', pistes_views.affiche),
    path('deletepistes/<int:id>/', pistes_views.delete),
    path('updatepistes/<int:id>/', pistes_views.update),
    path('updatetraitementpistes/<int:id>/', pistes_views.updatetraitement),

    #Urls pour la partie types d'avion
    path('indextypesavions/', typesavions_views.index),
    path('formulairetypesavions/', typesavions_views.formulaire),
    path('traitementtypesavions/', typesavions_views.traitement),
    path('affichetypesavions/<int:id>/', typesavions_views.affiche),
    path('deletetypesavions/<int:id>/', typesavions_views.delete),
    path('updatetypesavions/<int:id>/', typesavions_views.update),
    path('updatetraitementtypesavions/<int:id>/', typesavions_views.updatetraitement),

    #Urls pour la partie vols
    path('indexvols/', vols_views.index),
    path('formulairevols/', vols_views.formulaire),
    path('traitementvols/', vols_views.traitement),
    path('affichevols/<int:id>/', vols_views.affiche),
    path('deletevols/<int:id>/', vols_views.delete),
    path('updatevols/<int:id>/', vols_views.update),
    path('updatetraitementvols/<int:id>/', vols_views.updatetraitement),

]