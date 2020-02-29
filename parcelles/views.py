# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import ParcelleForm
from .models import Parcelle

def create(request):
    if request.method == "POST":
        form = ParcelleForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/parcelles/show")
            except:
                pass
    else:
        form = ParcelleForm()
    return render(request,'parcelles/index.html',{'form':form})

def show(request):
    parcelles = Parcelle.objects.all()
    return render(request,"parcelles/show.html",{'parcelles':parcelles})

def edit(request, numIlot):
    parcelle = Parcelle.objects.get(pk=numIlot)
    return render(request,'parcelles/edit.html', {'parcelle':parcelle})

def update(request, numIlot):
    parcelle = Parcelle.objects.get(pk=numIlot)
    form = ParcelleForm(request.POST, instance = parcelle)
    if form.is_valid():
        form.save()
        return redirect("/parcelles/show")
    return render(request, 'parcelles/edit.html', {'parcelles': parcelle})

def destroy(request, id):
    parcelle = Parcelle.objects.get(pk=id)
    parcelle.delete()
    return redirect("/parcelles/show")

def reset(request):
    Parcelle.objects.all().delete()
    parcelles = [Parcelle.objects.create(numIlot=10, nomParcelle="la parcelle", appellation="Chablis", domaine="Phil Goulley", surface=10.2),
                 Parcelle.objects.create(numIlot=20, nomParcelle="la parcelle2", appellation="Chablis2", domaine="Phil Goulley2", surface=11.2)]
    for parcelle in parcelles:
        form = ParcelleForm(request.POST, instance=parcelle)
        if form.is_valid():
            form.save()
    return redirect("/parcelles/show")
