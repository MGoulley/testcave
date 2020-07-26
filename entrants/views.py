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
        if not self.request.user.is_authenticated:
            return Parcelle.objects.none()

        qs = Parcelle.objects.all()
        if self.q:
            qs = qs.filter(nomParcelle__icontains=self.q)
        return qs

def parcelle_create(request):
    domaines = Organisation.objects.get(pk=request.session.get('organisation_id')).domaines.all()
    if request.method == "POST":
        post = request.POST.copy()
        parcelle = Parcelle.objects.create(numIlot = post["numIlot"], nomParcelle = post["nomParcelle"], 
                    appellation = post["appellation"], commune = post["commune"], refCadastre = post["refCadastre"], 
                    anneesPlantation = post["anneesPlantation"], datebio = post["datebio"])
        for i in range(len(post.getlist("domaine"))):
            parcelleEtendue = ParcelleEtendue(domaine=Domaine.objects.get(pk=post.getlist("domaine")[i]), parcelle=parcelle, proprietaire=post.getlist("proprietaire")[i], surface=post.getlist("surface")[i])
            parcelleEtendue.save()
        return redirect("/entrants/parcelles/show")
    form = ParcelleForm()
    return render(request,'parcelles/index.html',{'form':form, "domaines": domaines})


def parcelle_show(request):
    data = Parcelle.objects.all()
    return render(request,"parcelles/show.html",{'data':data})


def parcelle_edit(request, id):
    parcelle = Parcelle.objects.get(pk=id)
    form = ParcelleForm(request.POST or None, instance=parcelle)
    domaines = Organisation.objects.get(pk=request.session.get('organisation_id')).domaines.all()
    return render(request,'parcelles/edit.html', {'parcelle': parcelle, 'props':parcelle.parcelleetendue_set.all(), 'form': form, 'domaines': domaines})


def parcelle_update(request, id):
    post = request.POST.copy()
    parcelle = Parcelle.objects.get(pk=id)
    Parcelle.objects.filter(pk=id).update(numIlot = post["numIlot"], nomParcelle = post["nomParcelle"], 
                    appellation = post["appellation"], commune = post["commune"], refCadastre = post["refCadastre"], 
                    anneesPlantation = post["anneesPlantation"], datebio = post["datebio"])
    parcelle.domaines.clear()
    for i in range(len(post.getlist("domaine"))):
        parcelleEtendue = ParcelleEtendue(domaine=Domaine.objects.get(pk=post.getlist("domaine")[i]), parcelle=parcelle, proprietaire=post.getlist("proprietaire")[i], surface=post.getlist("surface")[i])
        parcelleEtendue.save()
    return redirect("/entrants/parcelles/show")


def parcelle_destroy(request, id):
    parcelle = Parcelle.objects.get(pk=id)
    parcelle.delete()
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
