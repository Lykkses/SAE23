from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class AeroportsForm(ModelForm):
    class Meta:
        model = models.Aeroports
        fields = ("id", "nom", "pays")
        labels = {
            "id" : _("Airport number"),
            "nom" : _("Airport name"),
            "pays" : _("Airport Country"),
        }

class PistesForm(ModelForm):
    class Meta:
        model = models.Pistes
        fields = ("numero", "aeroport", "longueur")
        labels = {
            "numero" : _("Track number"),
            "aeroport" : _("Airport"),
            "longueur" : _("The length of the landing strip"),
        }
class CompagniesForm(ModelForm):
    class Meta:
        model = models.Compagnies
        fields = ("id", "nom", "description", "pays_de_rattachement")
        labels = {
            "id" : _("Company number"),
            "nom" : _("Company Name"),
            "description" : _("Company Description"),
            "pays_de_rattachement" : _("The country of the airline"),
        }

class TypeavionForm(ModelForm):
    class Meta:
        model = models.Typeavions
        fields = ("id", "marque", "model", "description", "image", "longueurpistenecessaire")
        labels = {
            "id" : _("Aircraft number"),
            "marque" : _("Aircraft brand"),
            "model" : _("Aircraft model"),
            "description" : _("Description of the aircraft"),
            "image" : _("Airplane picture"),
            "longueurpistenecessaire" : _("Airstrip length"),
        }

class AvionsForm(ModelForm):
    class Meta:
        model = models.Avions
        fields = ("id", "nom", "compagnies", "model")
        labels = {
            "id" : _("Aircraft number"),
            "nom" : _("Aircraft name"),
            "compagnies" : _("Company Name"),
            "model" : _("Aircraft model"),
        }

class VolsForm(ModelForm):
    class Meta:
        model = models.Vols
        fields = ("id", "avions", "pilote", "aeroport_de_depart", "date_de_depart", "heure_de_depart", "aeroport_de_darriver", "date_de_darriver", "heure_de_darriver")
        labels = {
            "id" : _("Flight number"),
            "avions" : _("Aircraft model"),
            "pilote" : _("Driver's first and last name"),
            "aeroport_de_depart" : _("Departure airport name"),
            "date_de_depart" : _("Date of departure"),
            "heure_de_depart" : _("Departure time"),
            "aeroport_de_darriver" : _("Arrival airport name"),
            "date_de_darriver" : _("Arrival date"),
            "heure_de_darriver" : _("Arriving time"),
        }