# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dal import autocomplete
from .forms import *
from .models import *
from administration.models import Domaine

# PARCELLE
class ParcelleAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        print("Here")
        if not self.request.user.is_authenticated:
            return Parcelle.objects.none()

        qs = Parcelle.objects.all()
        print(qs)
        if self.q:
            qs = qs.filter(nomParcelle__istartswith=self.q)
        print(qs)
        return qs

def parcelle_create(request):
    data = Parcelle.objects.all()
    domaines = Domaine.objects.all()
    if request.method == "POST":
        post = request.POST.copy()
        post["domaine"] = Domaine.objects.get(id=request.POST.get("domaine"))
        request.POST = post
        form = ParcelleForm(request.POST)
        if form.is_valid():
            try:
                print("Save ?")
                form.save()
                print("Saved")
                return redirect("/entrants/parcelles/show")
            except:
                pass
        else:
            print("WTFFF")
    else:
        form = ParcelleForm()
    return render(request,'parcelles/index.html',{'form':form, "domaines": domaines})


def parcelle_show(request):
    data = Parcelle.objects.all()
    domaines = Domaine.objects.all()
    return render(request,"parcelles/show.html",{'data':data, "domaines": domaines})


def parcelle_edit(request, numIlot):
    parcelle = Parcelle.objects.get(pk=numIlot)
    return render(request,'parcelles/edit.html', {'parcelle':parcelle})


def parcelle_update(request, numIlot):
    parcelle = Parcelle.objects.get(pk=numIlot)
    form = ParcelleForm(request.POST, instance = parcelle)
    if form.is_valid():
        form.save()
        return redirect("/entrants/parcelles/show")
    return render(request, 'parcelles/edit.html', {'parcelles': parcelle})


def parcelle_destroy(request, numIlot):
    parcelle = Parcelle.objects.get(pk=numIlot)
    parcelle.delete()
    return redirect("/entrants/parcelles/show")


def parcelle_reset(request):
    Parcelle.objects.all().delete()
    parcelles = [Parcelle.objects.create(numIlot=10, nomParcelle="la parcelle", appellation="Chablis", domaine="Phil Goulley", surface=10.2),
                 Parcelle.objects.create(numIlot=20, nomParcelle="la parcelle2", appellation="Chablis2", domaine="Phil Goulley2", surface=11.2)]
    for parcelle in parcelles:
        form = ParcelleForm(request.POST, instance=parcelle)
        if form.is_valid():
            form.save()
    return redirect("/entrants/parcelles/show")


# MATERIEL
def materiel_create(request):
    if request.method == "POST":
        form = MaterielsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/entrants/materiels/show")
            except:
                pass
    else:
        form = MaterielsForm()
    return render(request,'materiels/index.html',{'form':form})


def materiel_show(request):
    materiels = Materiels.objects.all().filter(orga=request.session.get('organisation_id'))
    return render(request,"materiels/show.html",{'materiels':materiels})


def materiel_edit(request, id):
    materiel = Materiels.objects.get(id=id)
    return render(request,'materiels/edit.html', {'materiel':materiel})


def materiel_update(request, id):
    materiel = Materiels.objects.get(id=id)
    form = MaterielsForm(request.POST, instance = materiel)
    if form.is_valid():
        form.save()
        return redirect("/entrants/materiels/show")
    return render(request, 'materiels/edit.html', {'materiels': materiel})


def materiel_destroy(request, id):
    materiel = Materiels.objects.get(id=id)
    materiel.delete()
    return redirect("/entrants/materiels/show")
