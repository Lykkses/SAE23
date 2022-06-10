from django.shortcuts import render, HttpResponseRedirect
from . forms import TypesavionForm
from . import models


def formulaire(request):
    if request.method == "POST":
        form = TypesavionForm(request)
        return render(request, "basedonnees/typesavions/formulaire.html", {"form": form})
    else:
        form = TypesavionForm()
        id = ""
        return render(request, "basedonnees/typesavions/formulaire.html", {"form": form, "id": id})


def traitement(request):
    lform = TypesavionForm(request.POST)
    if lform.is_valid():
        typesavions = lform.save()

        return HttpResponseRedirect('/typesavions/indextypesavions/')
    else:
        return render(request, "basedonnees/typesavions/formulaire.html", {"form": lform})


def index(request):
    liste = list(models.Pistes.objects.all())
    return render(request, 'basedonnees/typesavions/index.html', {'liste': liste})


def affiche(request, id):
    typesavions = models.Pistes.objects.get(pk=id)
    liste = models.Avions.objects.filter(avions=id)
    return render(request, 'basedonnees/typesavions/affiche.html', {"typesavions": typesavions, 'liste': liste})


def update(request, id):
    typesavions = models.Typeavions.objects.get(pk=id)
    form = TypesavionForm(typesavions.dico())
    return render(request, 'basedonne/pistesatterissage/formulaire.html', {'form': form, 'id': id})


def updatetraitement(request, id):
    lform = TypesavionForm(request.POST)
    if lform.is_valid():
        typesavions = lform.save(commit=False)
        typesavions.id = id
        typesavions.save()
        return HttpResponseRedirect('/aeroports/indextypesavions/')
    else:
        return render(request, "basedonnees/typesavions/formulaire.html", {"form": lform, "id": id})


def delete(request, id):
    typesavions = models.Typeavions.objects.get(pk=id)
    typesavions.delete()
    return HttpResponseRedirect('/aeroports/indextypesavions/')