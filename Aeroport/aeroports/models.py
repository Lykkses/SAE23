from django.db import models

# Create your models here.
class Aeroports(models.Model):
    id = models.IntegerField(blank = False, primary_key=True)
    nom = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"L'aéroport {self.nom} situé en {self.nom}, possede l'ID {self.id}."
        return chaine

    def dico(self):
        return {"L'aéroport":self.nom, "situé en":self.pays, "possede l'ID":self.id}

class Pistes(models.Model):
    numero = models.IntegerField(blank = False)
    aeroport = models.CharField(max_length=100)
    longueur = models.IntegerField(blank = False)

    def __str__(self):
        chaine = f"La piste d'atterrissage numéro {self.numero} de l'aéroport {self.aeroport} à une longueur de {self.longueur} mètres."
        return chaine

    def dico(self):
        return {"La piste numéro":self.numero, "situé à l'aéroport":self.aeroport, "possede une piste d'une longueur de":self.longueur}

class Compagnies(models.Model):
    id = models.IntegerField(blank = False, primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.TextField(null = True, blank = True)
    pays_de_rattachement = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"{self.description}, le pays de rattachement de la compagnie est {self.pays_de_rattachement}."
        return chaine

    def dico(self):
        return {"":self.nom, "le pays de rattachement de la compagnie est ":self.pays_de_rattachement}

class Typeavions(models.Model):
    id = models.IntegerField(blank = False, primary_key=True)
    marque = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(null = True, blank = True)
    image = models.ImageField()
    longueurpistenecessaire = models.IntegerField(blank = False)


    def __str__(self):
        chaine = f"L'avion {self.model} de la marque {self.marque}, est {self.description}, il lui faut pour attérir une piste de {self.longueurpistenecessaire} mètre de long."
        return chaine

    def dico(self):
        return {"L'avion":self.model, "de la marque":self.marque, "est":self.description, "il lui faut pour attérir une piste de":self.longueurpistenecessaire}

class Avions(models.Model):
    id = models.IntegerField(blank = False, primary_key=True)
    nom = models.CharField(max_length=100)
    compagnies = models.CharField(max_length=100)
    model = models.CharField(max_length=100)


    def __str__(self):
        chaine = f"L'avion {self.model} de la marque {self.marque}, est {self.description}, il lui faut pour attérir une piste de {self.longueurpistenecessaire} mètre de long."
        return chaine

    def dico(self):
        return {"L'avion":self.model, "de la marque":self.marque, "est":self.description, "il lui faut pour attérir une piste de":self.longueurpistenecessaire}

class Vols(models.Model):
    id = models.IntegerField(blank = False, primary_key=True)
    avions = models.CharField(max_length=100)
    pilote = models.CharField(max_length=100)
    aeroport_de_depart = models.CharField(max_length=100)
    aeroport_de_darriver = models.CharField(max_length=100)
    date_de_depart = models.DateField(null=True, blank=True)
    date_de_darriver = models.DateField(null=True, blank=True)
    heure_de_depart = models.TimeField(auto_now=False, auto_now_add=False)
    heure_de_darriver = models.TimeField(auto_now=False, auto_now_add=False)


    def __str__(self):
        chaine = f"Le vol numéro {self.id} avec l'avion {self.avions} avec le pilote {self.pilote}, décollera à {self.heure_de_depart} le {self.date_de_depart} à {self.aeroport_de_depart}. Le vol et arrivera à destination à {self.heure_de_darriver}, le {self.date_de_darriver}, à {self.aeroport_de_darriver}."
        return chaine

    def dico(self):
        return {"Le vol numéro":self.id, "avec l'avion":self.avions, "avec le pilote":self.pilote, ", décollera à ":self.heure_de_depart, "le":self.date_de_depart, "à":self.aeroport_de_depart, "Le vol arrivera à destination à":self.heure_de_darriver, "le":self.date_de_darriver, "à l'aéroport de":self.aeroport_de_darriver}
