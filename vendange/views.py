# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from dal import autocomplete
from entrants.models import Parcelle
from entrants.models import Materiels
from django.utils.timezone import now

# BENNE

def benne_create(request):
    bennes = Materiels.objects.filter(type="BENNE").all()
    if request.method == "POST":
        post = request.POST.copy()
        print(post)
        parcelles = [Parcelle.objects.get(nomParcelle=nomParcelle) for nomParcelle in request.POST.getlist("parcelles")]
        print(parcelles)
        #post.setlist("parcelles", [Parcelle.objects.get(nomParcelle=nomParcelle) for nomParcelle in request.POST.getlist("parcelles")])
        request.POST = post
        form = BenneForm(request.POST)
        #print(form)
        if form.is_valid():
            try:
                print("Save ?")
                form.save()
                print("Saved")
                return redirect("/vendange/bennes/show")
            except:
                pass
    else:
        form = BenneForm()
        form.fields['idMillesime'].initial = request.session['millesime']
        form.fields['idBenne'].initial = Benne.objects.filter(idMillesime=request.session['millesime']).count() + 1
    print(form)
    return render(request,'bennes/index.html',{'form':form, 'lesbennes': bennes})

def benne_show(request):
    bennes = Benne.objects.all()
    parcelles = Parcelle.objects.all()
    return render(request,"bennes/show.html",{'bennes':bennes, 'lesparcelles':parcelles})


def benne_edit(request, id):
    benne = Benne.objects.get(id=id)
    parcelles = Parcelle.objects.all()
    benne.dateRecep = benne.dateRecep.strftime('%m/%d/%Y %H:%M')
    return render(request,'bennes/edit.html', {'benne':benne, 'lesparcelles': parcelles})


def benne_update(request, id):
    benne = Benne.objects.get(id=id)
    parcelles = Parcelle.objects.all()
    post = request.POST.copy()
    post.setlist("parcelles", [Parcelle.objects.get(numIlot=numIlot) for numIlot in request.POST.getlist("parcelles")])
    request.POST = post
    form = BenneForm(request.POST, instance=benne)
    if form.is_valid():
        form.save()
        return redirect("/bennes/show")
    else:
        benne = Benne.objects.get(id=id)
    return render(request, 'bennes/edit.html', {'benne': benne, 'lesparcelles': parcelles})


def benne_destroy(request, id):
    benne = Benne.objects.get(id=id)
    benne.delete()
    return redirect("/bennes/show")


def benne_reset(request):
    Benne.objects.all().delete()
    # benne=Benne(idBenne=1, idMillesime=2021, dateRecep="2020-02-27 22:32", densite=20.8, temperature=10.2, alcProb=20.0, so2=0.25, autre1="", autre2="", meteo="AAA", pourcentSO2=0.321, idOperateur=1, idMateriel=1)
    # benne.save()
    # benne.parcelles.add(Parcelle.objects.all()[0])
    # benne.save()
    return redirect("/bennes/show")




# MARCS


def marcs_create(request):
    parcelles = Parcelle.objects.all()
    bennes = Materiels.objects.filter(type="BENNE").all()
    if request.method == "POST":
        post = request.POST.copy()
        post.setlist("parcelles", [Parcelle.objects.get(numIlot=numIlot) for numIlot in request.POST.getlist("parcelles")])
        request.POST = post
        form = BenneForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/bennes/show")
            except:
                pass
    else:
        form = BenneForm()
        form.fields['idMillesime'].initial = request.session['millesime']
        form.fields['idBenne'].initial = Benne.objects.filter(idMillesime=request.session['millesime']).count() + 1
    return render(request,'bennes/index.html',{'form':form, 'lesparcelles': parcelles, 'lesbennes': bennes})


def marcs_show(request):
    bennes = Benne.objects.all()
    parcelles = Parcelle.objects.all()
    return render(request,"bennes/show.html",{'bennes':bennes, 'lesparcelles':parcelles})


def marcs_edit(request, id):
    benne = Benne.objects.get(id=id)
    parcelles = Parcelle.objects.all()
    benne.dateRecep = benne.dateRecep.strftime('%m/%d/%Y %H:%M')
    return render(request,'bennes/edit.html', {'benne':benne, 'lesparcelles': parcelles})


def marcs_update(request, id):
    benne = Benne.objects.get(id=id)
    parcelles = Parcelle.objects.all()
    post = request.POST.copy()
    post.setlist("parcelles", [Parcelle.objects.get(numIlot=numIlot) for numIlot in request.POST.getlist("parcelles")])
    request.POST = post
    form = BenneForm(request.POST, instance=benne)
    if form.is_valid():
        form.save()
        return redirect("/bennes/show")
    else:
        benne = Benne.objects.get(id=id)
    return render(request, 'bennes/edit.html', {'benne': benne, 'lesparcelles': parcelles})


def marcs_destroy(request, id):
    benne = Benne.objects.get(id=id)
    benne.delete()
    return redirect("/bennes/show")
