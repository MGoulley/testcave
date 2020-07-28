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

    """ try:
        benne = Benne.objects.get(pk=id)
        Benne.objects.filter(pk=id).update(benne = Materiels.objects.get(
            pk=post['idMateriel']),
            idBenne = post['idBenne'], 
            dateRecep = strptime(post['dateRecep'], '%m/%d/%Y %H:%M'), 
            densite = post['densite'],
            temperature = post['temperature'], 
            alcProb = post['alcProb'], 
            so2 = post['so2'], 
            commentaire = post['commentaire'],
            meteo = post['meteo'], 
            pourcentSO2 = post['pourcentSO2'])
        benne.parcelles.clear() 
        for parcelle in [Parcelle.objects.get(domaines__in=Organisation.objects.get(pk=request.session.get('organisation_id')).domaines.all() ,nomParcelle=nomParcelle) for nomParcelle in request.POST.getlist("parcelles")]:
            benne.parcelles.add(parcelle.id)
        return redirect("/vendange/bennes/show")
    except:
        return redirect("/vendange/bennes/edit/" + str(id)) """

def benne_destroy(request, id):
    benne = Benne.objects.get(id=id)
    benne.delete()
    return redirect("/vendange/bennes/show")

# MARCS
def marcs_create(request):
    pressoires = Materiels.objects.filter(type="PRESSOIRE").all()
    if request.method == "POST":
        post = request.POST.copy()

        form = MarcForm(post)
        if form.is_valid():
            try:
                form.save()
                return redirect("/marcs/show")
            except:
                pass
    else:
        form = MarcForm()
        form.fields['millesime'].initial = request.session['millesime']
        form.fields['idMarc'].initial = Marc.objects.filter(millesime=request.session['millesime']).count() + 1
    return render(request,'marcs/index.html',{'form':form, 'lespressoires': pressoires})


def marcs_show(request):
    data = Marc.objects.all()
    return render(request,"marcs/show.html",{'data':data})


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
