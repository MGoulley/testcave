# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
import datetime
from dal import autocomplete
from entrants.models import Parcelle
from entrants.models import Materiels
from administration.models import Domaine
from django.utils.timezone import now
from django.db.models import Max
import bs4

# BENNE

def benne_create(request):
    bennes = Materiels.objects.filter(orga=request.session.get('organisation_id'), type="BENNE").all()
    if request.method == "POST":
        post = request.POST.copy()
        post['millesime'] = Millesime.objects.get(annee=request.session['millesime'])
        parcelles = [Parcelle.objects.filter(domaines__in = Organisation.objects.get(pk=request.session.get('organisation_id')).domaines.all(), nomParcelle=nomParcelle) for nomParcelle in request.POST.getlist("parcelles")]
        benne = Benne.objects.create(orga = Organisation.objects.get(pk=request.session.get('organisation_id')), millesime = Millesime.objects.get(annee=request.session['millesime']), operateur = request.user, benne = Materiels.objects.get(pk=post['idMateriel']),
            idBenne = post['idBenne'], dateRecep = datetime.datetime.strptime(post['dateRecep'], '%m/%d/%Y %H:%M'), densite = post['densite'],
            temperature = post['temperature'], alcProb = post['alcProb'], so2 = post['so2'], commentaire = post['commentaire'],
            meteo = post['meteo'], pourcentSO2 = post['pourcentSO2'])

        for parcelle in parcelles:
            benne.parcelles.add(parcelle)
        return redirect("/vendange/bennes/show")

    else:
        form = BenneForm()
        form.fields['millesime'].initial = request.session['millesime']
        form.fields['idBenne'].initial = Benne.objects.filter(millesime=request.session['millesime']).aggregate(Max('idBenne'))['idBenne__max'] + 1
    return render(request,'bennes/index.html',{'form':form, 'lesbennes': bennes})

def benne_show(request):
    bennes = Benne.objects.filter(orga=request.session.get('organisation_id'), millesime=Millesime.objects.get(annee=request.session['millesime']))
    return render(request,"bennes/show.html",{'bennes':bennes})

def benne_edit(request, id):
    benne = Benne.objects.get(id=id)
    form = BenneForm(request.POST or None, instance=benne)
    form.fields['parcelles'].to_field_name="nomParcelle"
    benne.dateRecep = benne.dateRecep.strftime('%m/%d/%Y %H:%M')
    bennes = Materiels.objects.filter(orga=request.session.get('organisation_id'), type="BENNE").all()
    return render(request,'bennes/edit.html', {'benne':benne, 'lesbennes': bennes, 'form': form})


def benne_update(request, id):
    post = request.POST.copy()
    print(post)
    print(Materiels.objects.all())
    print(Materiels.objects.get(pk=post['idMateriel']))
    benne = Benne.objects.filter(pk=id).update(benne = Materiels.objects.get(pk=post['idMateriel']),
            idBenne = post['idBenne'], dateRecep = datetime.datetime.strptime(post['dateRecep'], '%m/%d/%Y %H:%M'), densite = post['densite'],
            temperature = post['temperature'], alcProb = post['alcProb'], so2 = post['so2'], commentaire = post['commentaire'],
            meteo = post['meteo'], pourcentSO2 = post['pourcentSO2'])

    benne.parcelles.clear()
    for parcelle in post.getlist("parcelles"):
        #parcelle = Parcelle.domaines.filter(domaine__in=)
        parcelleEtendue = ParcelleEtendue(domaine=Domaine.objects.get(pk=post.getlist("domaine")[i]), parcelle=parcelle, proprietaire=post.getlist("proprietaire")[i], surface=post.getlist("surface")[i])
        parcelleEtendue.save()
        benne.parcelles.add(parcelle)
    return render(request, 'bennes/edit.html', {'benne': benne, 'lesparcelles': parcelles})

"""     benne = Benne.objects.get(id=id)
    parcelles = Parcelle.objects.all()
    post = request.POST.copy()
    post.setlist("parcelles", [Parcelle.objects.filter(domaines__in= ,nomParcelle=nomParcelle) for nomParcelle in request.POST.getlist("parcelles")])
    request.POST = post
    form = BenneForm(request.POST, instance=benne)
    if form.is_valid():
        form.save()
        return redirect("/vendange/bennes/show")
    else:
        benne = Benne.objects.get(id=id) """
    


def benne_destroy(request, id):
    benne = Benne.objects.get(id=id)
    benne.delete()
    return redirect("/vendange/bennes/show")

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
