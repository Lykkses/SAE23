from django.shortcuts import render, HttpResponseRedirect
from . forms import AvionsForm
from . import models


def formulaire(request):
    if request.method == "POST":
        form = AvionsForm(request)
        return render(request, "basedonnees/avions/formulaire.html", {"form": form})
    else:
        form = AvionsForm()
        id = ""
        return render(request, "basedonnees/avions/formulaire.html", {"form": form, "id": id})


def traitement(request):
    lform = AvionsForm(request.POST)
    if lform.is_valid():
        avions = lform.save()

        return HttpResponseRedirect('/indexavions/')
    else:
        return render(request, "/avions/formulaire.html", {"form": lform})


def index(request):
    liste = list(models.Avions.objects.all())
    return render(request, 'basedonnees/avions/index.html', {'liste': liste})


def affiche(request, id):
    avions = models.Avions.objects.get(pk=id)
    liste = models.Typeavions.objects.filter(avions_id=id)
    liste2 = models.Compagnies.objects.filter(avions_id=id)
    return render(request, 'basedonnees/avions/affiche.html', {"avions": avions, 'liste': liste, 'liste2': liste2})


def update(request, id):
    avions = models.Avions.objects.get(pk=id)
    form = AvionsForm(avions.dico())
    return render(request, 'basedonnees/avions/formulaire.html', {'form': form, 'id': id})


def updatetraitement(request, id):
    lform = AvionsForm(request.POST)
    if lform.is_valid():
        avions = lform.save(commit=False)
        avions.id = id
        avions.save()
        return HttpResponseRedirect('/indexavions/')
    else:
        return render(request, "basedonnees/avions/formulaire.html", {"form": lform, "id": id})


def delete(request, id):
    avions = models.Avions.objects.get(pk=id)
    avions.delete()
    return HttpResponseRedirect('/aeroports/indexavions/')