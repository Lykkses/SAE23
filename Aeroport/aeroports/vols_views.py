from django.shortcuts import render, HttpResponseRedirect
from . forms import VolsForm
from . import models


def formulaire(request):
    if request.method == "POST":
        form = VolsForm(request)
        return render(request, "basedonnees/vols/formulaire.html", {"form": form})
    else:
        form = VolsForm()
        id = ""
        return render(request, "basedonnees/vols/formulaire.html", {"form": form, "id": id})


def traitement(request):
    lform = VolsForm(request.POST)
    if lform.is_valid():
        lform.save()
        return HttpResponseRedirect('/indexvols/')
    else:
        return render(request, "basedonnees/vols/formulaire.html", {"form": lform})


def index(request):
    liste = list(models.Vols.objects.all())
    return render(request, 'basedonnees/vols/index.html', {'liste': liste})


def affiche(request, id):
    vols = models.Vols.objects.get(pk=id)
    liste = models.Vols.objects.filter(avions=id)
    return render(request, 'basedonnees/vols/affiche.html', {"vols": vols, 'liste': liste})


def update(request, id):
    vols = models.Vols.objects.get(pk=id)
    form = VolsForm(vols.dico())
    return render(request, 'basedonnees/vols/update.html', {'form': form, 'id': id})


def updatetraitement(request, id):
    lform = VolsForm(request.POST)
    if lform.is_valid():
        vols = lform.save(commit=False)
        vols.id = id
        vols.save()
        return HttpResponseRedirect('/aeroports/indexvols/')
    else:
        return render(request, "basedonnees/vols/update.html", {"form": lform, "id": id})


def delete(request, id):
    vols = models.Vols.objects.get(pk=id)
    vols.delete()
    return HttpResponseRedirect('/aeroports/indexvols/')
