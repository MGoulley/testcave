# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.utils.timezone import now

# DOMAINE
def domaine_create(request):
    if request.method == "POST":
        form = DomaineForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/administration/domaines/show")
            except:
                pass
    else:
        form = DomaineForm()
    return render(request,'domaines/index.html',{'form':form})

def domaine_show(request):
    data = Organisation.objects.get(pk=request.session.get('organisation_id')).domaines.all()
    return render(request,"domaines/show.html",{'data':data})

def domaine_edit(request, id):
    data = Domaine.objects.get(pk=id)
    return render(request,'domaines/edit.html', {'data':data})

def domaine_update(request, id):
    data = Domaine.objects.get(pk=id)
    form = DomaineForm(request.POST, instance = data)
    if form.is_valid():
        form.save()
        return redirect("/administration/domaines/show")
    return render(request, 'domaines/edit.html', {'data': data})

def domaine_destroy(request, id):
    data = Domaine.objects.get(pk=id)
    data.delete()
    return redirect("/administration/domaines/show")


# MILLESIME
def millesime_create(request):
    if request.method == "POST":
        form = MillesimeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/administration/millesimes/show")
            except:
                pass
    else:
        form = MillesimeForm()
    return render(request,'millesimes/index.html',{'form':form})

def millesime_show(request):
    millesimes = Millesime.objects.all().filter(orga=request.session.get('organisation_id'))
    return render(request,"millesimes/show.html",{'millesimes':millesimes})

def millesime_edit(request, annee):
    millesime = Millesime.objects.get(pk=annee)
    return render(request,'millesimes/edit.html', {'millesime':millesime})

def millesime_update(request, annee):
    millesime = Millesime.objects.get(pk=annee)
    form = MillesimeForm(request.POST, instance = millesime)
    if form.is_valid():
        form.save()
        return redirect("/administration/millesimes/show")
    return render(request, 'millesimes/edit.html', {'millesimes': millesime})

def millesime_destroy(request, annee):
    millesime = Millesime.objects.get(pk=annee)
    millesime.delete()
    return redirect("/administration/millesimes/show")



