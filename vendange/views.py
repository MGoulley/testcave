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
            benne.parcelles.add(parcelle[0].id)
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
    benne = Benne.objects.get(pk=id)
    Benne.objects.filter(pk=id).update(benne = Materiels.objects.get(
        pk=post['idMateriel']),
        idBenne = post['idBenne'], 
        dateRecep = datetime.datetime.strptime(post['dateRecep'],'%m/%d/%Y %H:%M'), 
        densite = post['densite'],
        temperature = post['temperature'], 
        alcProb = post['alcProb'], 
        so2 = post['so2'], 
        commentaire = post['commentaire'],
        meteo = post['meteo'], 
        pourcentSO2 = post['pourcentSO2'])
    benne.parcelles.clear() 
    for parcelle in [Parcelle.objects.filter(domaines__in=Organisation.objects.get(pk=request.session.get('organisation_id')).domaines.all() ,nomParcelle=nomParcelle) for nomParcelle in request.POST.getlist("parcelles")]:
        benne.parcelles.add(parcelle[0].id)
    return redirect("/vendange/bennes/show")

def benne_destroy(request, id):
    benne = Benne.objects.get(id=id)
    benne.delete()
    return redirect("/vendange/bennes/show")

# MARCS
def marcs_create(request):
    pressoires = Materiels.objects.filter(orga=Organisation.objects.get(pk=request.session.get('organisation_id')), type="PRESSOIR").all()
    bennes = Benne.objects.filter(orga=Organisation.objects.get(pk=request.session.get('organisation_id')), millesime=request.session['millesime'])
    if request.method == "POST":
        post = request.POST.copy()
        print(post)
        marc = Marc.objects.create(orga = Organisation.objects.get(pk=request.session.get('organisation_id')), 
            millesime = Millesime.objects.get(annee=request.session['millesime']), 
            idMarc = post['idMarc'],
            volumeMarc = post['volumeMarc'], 
            pressoire = Materiels.objects.get(pk=post['pressoire']))

        print("Bennes : ")
        for i in range(len(post.getlist("benne"))):
            benneMarc = BennesMarc(marc=marc, benne=Benne.objects.get(id=post.getlist("benne")[i]), volBenne=post.getlist("volBenne")[i])
            benneMarc.save()

        return redirect("/vendange/marcs/show")
    else:
        form = MarcForm()
        form.fields['millesime'].initial = request.session['millesime']
        form.fields['idMarc'].initial = Marc.objects.filter(millesime=request.session['millesime']).count() + 1
    return render(request,'marcs/index.html',{'form':form, 'lespressoires': pressoires, 'lesbennes': bennes})


def marcs_show(request):
    data = Marc.objects.all()
    return render(request,"marcs/show.html",{'data':data})


def marcs_edit(request, id):
    data = Marc.objects.get(id=id)
    pressoires = Materiels.objects.filter(orga=Organisation.objects.get(pk=request.session.get('organisation_id')), type="PRESSOIR").all()
    bennes = data.bennesmarc_set.all()
    lesbennes = Benne.objects.filter(orga=request.session.get('organisation_id'), millesime=Millesime.objects.get(annee=request.session['millesime']))
    return render(request,'marcs/edit.html', {'data':data, 'lespressoires': pressoires, 'lesbennes': lesbennes, 'bennes': bennes})


def marcs_update(request, id):
    post = request.POST.copy()
    print(post)
    marc = Marc.objects.get(id=id)
    Marc.objects.filter(pk=id).update(volumeMarc=post['volumeMarc'], pressoire = Materiels.objects.get(pk=post['pressoire']))
    marc.bennes.clear()
    for i in range(len(post.getlist("benne"))):
        bennesmarc = BennesMarc(marc=marc, benne=Benne.objects.get(id=post.getlist("benne")[i]), volBenne=post.getlist("volBenne")[i])
        bennesmarc.save()
    return redirect("/vendange/marcs/show")


def marcs_destroy(request, id):
    data = Marc.objects.get(id=id)
    data.delete()
    return redirect("/vendange/marcs/show")
