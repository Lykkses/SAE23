from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class AeroportsForm(ModelForm):
    class Meta:
        model = models.Groupedemetal
        fields = ('registre', 'sous_registre', 'nom_du_groupe', 'nationalite', 'annee_de_creation', 'nombre_album', 'courte_description', 'typedemetal')
        labels = {
            'registre' : _('Registre'),
            'sous_registre' : _('Sous registre'),
            'nom_du_groupe' : _('Nom du groupe'),
            'nationalite' : _('Nationalité'),
            'annee_de_creation' : _('Année de création'),
            'nombre_album' : _('Nombre album'),
            'courte_description' : _('Courte description'),
            'typedemtal' : _('Type de metal'),
        }