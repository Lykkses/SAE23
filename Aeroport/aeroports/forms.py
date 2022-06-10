from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class AeroportsForm(ModelForm):
    class Meta:
        model = models.Aeroports
        fields = ("id", "nom", "pays")
        labels = {
            "id" : _("Numéro de l'aéroport"),
            "nom" : _("Nom de l'aéroport"),
            "pays" : _("Pays de l'aéroport"),
        }

class PistesForm(ModelForm):
    class Meta:
        model = models.Pistes
        fields = ("numero", "aeroport", "longueur")
        labels = {
            "numero" : _("Numéro de piste"),
            "aeroport" : _("Aeroport"),
            "longueur" : _("L'ongueur de la piste d'attérissage"),
        }
class CompagniesForm(ModelForm):
    class Meta:
        model = models.Compagnies
        fields = ("id", "nom", "description", "pays_de_rattachement")
        labels = {
            "id" : _("Numéro de la compagnie"),
            "nom" : _("Nom de la compagnie"),
            "description" : _("Description de la compagnie"),
            "pays_de_rattachement" : _("Le pays de la compagnie aérienne"),
        }

class TypesavionForm(ModelForm):
    class Meta:
        model = models.Typeavions
        fields = ("id", "marque", "model", "description", "image", "longueurpistenecessaire")
        labels = {
            "id" : _("Numéro de l'avion"),
            "marque" : _("Marque de l'avion"),
            "model" : _("Model de l'avion"),
            "description" : _("Description de l'avion"),
            "image" : _("Image de l'avion"),
            "longueurpistenecessaire" : _("Longueur de la piste d'attérissage"),
        }

class AvionsForm(ModelForm):
    class Meta:
        model = models.Avions
        fields = ("id", "nom", "compagnies", "model")
        labels = {
            "id" : _("Numéro d'avion"),
            "nom" : _("Nom de l'avion"),
            "compagnies" : _("Nom de la compagnie"),
            "model" : _("Model de l'avion"),
        }

class VolsForm(ModelForm):
    class Meta:
        model = models.Vols
        fields = ("id", "avions", "pilote", "aeroport_de_depart", "date_de_depart", "heure_de_depart", "aeroport_de_darriver", "date_de_darriver", "heure_de_darriver")
        labels = {
            "id" : _("Numéro de vol"),
            "avions" : _("Modèle de l'avion"),
            "pilote" : _("Nom et prénom du pilote"),
            "aeroport_de_depart" : _("Nom de l'aéroport de départ"),
            "date_de_depart" : _("Date de départ"),
            "heure_de_depart" : _("Heure de départ"),
            "aeroport_de_darriver" : _("Nom de l'aéroport d'arriver"),
            "date_de_darriver" : _("Date d'arriver"),
            "heure_de_darriver" : _("Heure d'arriver"),
        }