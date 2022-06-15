from django.shortcuts import render, HttpResponseRedirect
from . forms import PistesForm
from . import models


def formulaire(request):
    if request.method == "POST":
        form = PistesForm(request)
        return render(request, "basedonnees/pistesatterissage/formulaire.html", {"form": form})
    else:
        form = PistesForm()
        id = ""
        return render(request, "basedonnees/pistesatterissage/formulaire.html", {"form": form, "id": id})


def traitement(request):
    lform = PistesForm(request.POST)
    if lform.is_valid():
        lform.save()
        return HttpResponseRedirect('/indexpistes/')
    else:
        return render(request, "basedonnees/pistesatterissage/formulaire.html", {"form": lform})


def index(request):
    liste = list(models.Pistes.objects.all())
    return render(request, 'basedonnees/pistesatterissage/index.html', {'liste': liste})


def affiche(request, id):
    pistesatterissage = models.Pistes.objects.get(pk=id)
    return render(request, 'basedonnees/pistesatterissage/affiche.html', {"pistesatterissage": pistesatterissage})


def update(request, id):
    pistesatterissage = models.Pistes.objects.get(pk=id)
    form = PistesForm(pistesatterissage.dico())
    return render(request, 'basedonnees/pistesatterissage/update.html', {'form': form, 'id': id})


def updatetraitement(request, id):
    lform = PistesForm(request.POST)
    if lform.is_valid():
        pistesatterissage = lform.save(commit=False)
        pistesatterissage.id = id
        pistesatterissage.save()
        return HttpResponseRedirect('/indexpistes/')
    else:
        return render(request, "basedonnees/pistesatterissage/update.html", {"form": lform, "id": id})


def delete(request, id):
    pistesatterissage = models.Pistes.objects.get(pk=id)
    pistesatterissage.delete()
    return HttpResponseRedirect('/aeroports/indexpistes/')