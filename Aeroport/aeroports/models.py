from django.db import models

# Create your models here.
class Aeroports(models.Model):
    id = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"L'aéroport {self.nom} situé en {self.nom}, possede l'ID {self.id}."
        return chaine

    def dico(self):
        return {"L'aéroport":self.nom, "situé en":self.pays, "possede l'ID":self.id}
