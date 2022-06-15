from django.db import models

# Create your models here.
class Aeroports(models.Model):
    #id = models.IntegerField(blank = False, primary_key=True)
    nom = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)


    def __str__(self):
        chaine = f"The airport {self.nom} located in {self.pays}, has the ID {self.id}."
        return chaine

    def dico(self):
        return {"nom":self.nom, "pays":self.pays, "id":self.id}

class Pistes(models.Model):
    #id = models.IntegerField(blank = False, primary_key=True)
    numero = models.IntegerField(blank = False)
    aeroport = models.CharField(max_length=100)
    longueur = models.IntegerField(blank = False)

    def __str__(self):
        chaine = f"The runway number {self.numero} of the airport {self.aeroport} has a length of {self.longueur} meters."
        return chaine

    def dico(self):
        return {"id":self.id,"numero":self.numero, "aeroport":self.aeroport, "plongueur":self.longueur}

class Compagnies(models.Model):
    #id = models.IntegerField(blank = False, primary_key=True)
    nom = models.CharField(max_length=100)
    description = models.TextField(null = True, blank = True)
    pays_de_rattachement = models.CharField(max_length=100)

    def __str__(self):
        chaine = f"{self.description}. The country of attachment of the company is {self.pays_de_rattachement}."
        return chaine

    def dico(self):
        return {"nom":self.nom,"description":self.description, "pays_de_rattachement":self.pays_de_rattachement}

class Typeavions(models.Model):
    #id = models.IntegerField(blank = False, primary_key=True)
    marque = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(null = True, blank = True)
    image = models.ImageField(upload_to = "image")
    longueurpistenecessaire = models.IntegerField(blank = False)


    def __str__(self):
        chaine = f"The plane {self.model} of the brand {self.marque}, is {self.description}, it needs to land a runway of {self.longueurpistenecessaire} meter long."
        return chaine

    def dico(self):
        return {"model":self.model, "marque":self.marque, "description":self.description, "longueurpistenecessaire":self.longueurpistenecessaire}

class Avions(models.Model):
    #id = models.IntegerField(blank = False, primary_key=True)
    nom = models.CharField(max_length=100)
    compagnies = models.CharField(max_length=100)
    model = models.CharField(max_length=100)


    def __str__(self):
        chaine = f"The plane {self.id} the company {self.compagnies}, is a {self.nom}{self.model}."
        return chaine

    def dico(self):
        return {"is":self.id, "nom":self.nom, "compagnies":self.compagnies, "model":self.model}

class Vols(models.Model):
    #id = models.IntegerField(blank = False, primary_key=True)
    #avions = models.CharField(max_length=100)
    avions = models.ForeignKey(Avions, on_delete = models.CASCADE)
    pilote = models.CharField(max_length=100)
    #aeroport_de_depart = models.CharField(max_length=100)
    aeroport_de_depart = models.ForeignKey(Aeroports, on_delete = models.CASCADE, related_name = "Aeroport_Depart")
    #aeroport_de_darriver = models.CharField(max_length=100)
    aeroport_de_darriver = models.ForeignKey(Aeroports, on_delete = models.CASCADE, related_name = "Aeroport_Arrivee")
    date_de_depart = models.DateField(null=True, blank=True)
    date_de_darriver = models.DateField(null=True, blank=True)
    heure_de_depart = models.TimeField(auto_now=False, auto_now_add=False)
    heure_de_darriver = models.TimeField(auto_now=False, auto_now_add=False)



    def __str__(self):
        chaine = f"Flight number {self.id} with the plane {self.avions} with the pilot {self.pilote}, will take off at {self.heure_de_depart} the {self.date_de_depart} at {self.aeroport_de_depart}. The flight and will arrive at its destination at {self.heure_de_darriver}, the {self.date_de_darriver}, at {self.aeroport_de_darriver}."
        return chaine

    def dico(self):
        return {"id":self.id, "avions":self.avions, "pilote":self.pilote, "heure_de_depart":self.heure_de_depart, "date_de_depart":self.date_de_depart, "aeroport_de_depart":self.aeroport_de_depart, "heure_de_darriver":self.heure_de_darriver, "date_de_darriver":self.date_de_darriver, "aeroport_de_darriver":self.aeroport_de_darriver}
