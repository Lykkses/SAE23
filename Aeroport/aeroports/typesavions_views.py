from django.shortcuts import render, HttpResponseRedirect
from . forms import TypeavionForm
from . import models


def formulaire(request):
    if request.method == "POST":
        form = TypeavionForm(request)
        return render(request, "basedonnees/typesavions/formulaire.html", {"form": form})
    else:
        form = TypeavionForm()
        id = ""
        return render(request, "basedonnees/typesavions/formulaire.html", {"form": form, "id": id})


def traitement(request):
    lform = TypeavionForm(request.POST, request.FILES)
    if lform.is_valid():
        lform.save()
        return HttpResponseRedirect('/indextypesavions/')
    else:
        return render(request, "basedonnees/typesavions/formulaire.html", {"form": lform})


def index(request):
    liste = list(models.Typeavions.objects.all())
    return render(request, 'basedonnees/typesavions/index.html', {'liste': liste})


def affiche(request, id):
    typesavions = models.Typeavions.objects.get(pk=id)
    liste = models.Avions.objects.filter(avions=id)
    return render(request, 'basedonnees/typesavions/affiche.html', {"typesavions": typesavions, 'liste': liste})


def update(request, id):
    typesavions = models.Typeavions.objects.get(pk=id)
    form = TypeavionForm(typesavions.dico())
    return render(request, 'basedonnees/typesavions/update.html', {'form': form, 'id': id})


def updatetraitement(request, id):
    lform = TypeavionForm(request.POST, request.FILES)
    if lform.is_valid():
        typesavions = lform.save(commit=False)
        typesavions.id = id
        typesavions.save()
        return HttpResponseRedirect('/indextypesavions/')
    else:
        return render(request, "basedonnees/typesavions/update.html", {"form": lform, "id": id})


def delete(request, id):
    typesavions = models.Typeavions.objects.get(pk=id)
    typesavions.delete()
    return HttpResponseRedirect('/aeroports/indextypesavions/')