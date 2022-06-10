from django.shortcuts import render, HttpResponseRedirect
from . forms import CompagniesForm
from . import models


def formulaire(request):
    if request.method == "POST":
        form = CompagniesForm(request)
        return render(request, "basedonnees/compagnies/formulaire.html", {"form": form})
    else:
        form = CompagniesForm()
        id = ""
        return render(request, "basedonnees/compagnies/formulaire.html", {"form": form, "id": id})


def traitement(request):
    lform = CompagniesForm(request.POST)
    if lform.is_valid():
        compagnies = lform.save()

        return HttpResponseRedirect('/compagnies/indexcompagnies/')
    else:
        return render(request, "basedonnees/compagnies/formulaire.html", {"form": lform})


def index(request):
    liste = list(models.Compagnies.objects.all())
    return render(request, 'basedonnees/compagnies/index.html', {'liste': liste})


def affiche(request, id):
    compagnies = models.Compagnies.objects.get(pk=id)
    liste = models.Compagnies.objects.filter(compagnies=id)
    return render(request, 'basedonnees/compagnies/affiche.html', {"compagnies": compagnies, 'liste': liste})


def update(request, id):
    compagnies = models.Compagnies.objects.get(pk=id)
    form = CompagniesForm(compagnies.dico())
    return render(request, 'basedonne/compagnies/formulaire.html', {'form': form, 'id': id})


def updatetraitement(request, id):
    lform = CompagniesForm(request.POST)
    if lform.is_valid():
        compagnies = lform.save(commit=False)
        compagnies.id = id
        compagnies.save()
        return HttpResponseRedirect('/aeroports/indexcompagnies/')
    else:
        return render(request, "basedonnees/compagnies/formulaire.html", {"form": lform, "id": id})


def delete(request, id):
    compagnies = models.Compagnies.objects.get(pk=id)
    compagnies.delete()
    return HttpResponseRedirect('/aeroports/indexcompagnies/')