from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
import datetime
from administration.models import Domaine
from administration.models import Organisation

import json
from django.core.serializers.json import DjangoJSONEncoder

# LOT
def lot_create(request):
    orga = Organisation.objects.get(pk=request.session.get('organisation_id'))
    millesime=request.session.get('millesime')
    if request.method == "POST":
        post = request.POST.copy()
        print(post)
        post['millesime'] = Millesime.objects.get(annee=millesime)
        lot = Lot.objects.create(nom = post["nom"], volume = post["volume"], orga = orga,
                    millesime = post["millesime"], dateCreation = datetime.datetime.strptime(post["dateCreation"], '%m/%d/%Y %H:%M'))
        for i in range(len(post.getlist("marc"))):
            marcsLots = MarcsLots(marc=Marc.objects.get(orga=orga, millesime=millesime, idMarc=post.getlist("marc")[i]), lot=lot, volume=post.getlist("volume")[i])
            marcsLots.save()
        return redirect("/cave/lots/show")
    form = LotForm()
    form.fields['millesime'].initial = millesime
    marcs = Marc.objects.filter(orga=orga, millesime=millesime)
    return render(request,'lots/index.html',{'form':form, 'marcs':marcs})


def lot_show(request):
    data = Lot.objects.all()
    return render(request,"lots/show.html",{'data':data})


def lot_edit(request, id):
    lot = Lot.objects.get(pk=id)
    form = LotForm(request.POST or None, instance=lot)
    orga = Organisation.objects.get(pk=request.session.get('organisation_id'))
    millesime=request.session.get('millesime')
    marcs = Marc.objects.filter(orga=orga, millesime=millesime)
    return render(request,'lots/edit.html', {'lot': lot, 'form': form, 'marcs': marcs})


def lot_update(request, id):
    post = request.POST.copy()
    print(post)
    lot = Lot.objects.get(pk=id)
    millesime=request.session.get('millesime')
    orga = Organisation.objects.get(pk=request.session.get('organisation_id'))
    post['millesime'] = Millesime.objects.get(annee=millesime)
    Lot.objects.filter(pk=id).update(nom = post["nom"], volume = post["volume"], orga = orga,
                    millesime = post["millesime"], dateCreation = datetime.datetime.strptime(post["dateCreation"], '%m/%d/%Y %H:%M'))
    lot.marc.clear()
    for i in range(len(post.getlist("marcs"))):
        marcsLots = MarcsLots(marc=Marc.objects.get(orga=orga, millesime=millesime, idMarc=post.getlist("marcs")[i]), lot=lot, volume=post.getlist("volumes")[i])
        marcsLots.save()
    return redirect("/cave/lots/show")


def lot_destroy(request, id):
    data = Lot.objects.get(pk=id)
    data.delete()
    return redirect("/cave/lots/show")
