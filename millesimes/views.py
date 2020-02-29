# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import MillesimeForm
from .models import Millesime

def create(request):
    if request.method == "POST":
        form = MillesimeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/millesimes/show")
            except:
                pass
    else:
        form = MillesimeForm()
    return render(request,'millesimes/index.html',{'form':form})

def show(request):
    millesimes = Millesime.objects.all()
    return render(request,"millesimes/show.html",{'millesimes':millesimes})

def edit(request, annee):
    millesime = Millesime.objects.get(pk=annee)
    return render(request,'millesimes/edit.html', {'millesime':millesime})

def update(request, annee):
    millesime = Millesime.objects.get(pk=annee)
    form = MillesimeForm(request.POST, instance = millesime)
    if form.is_valid():
        form.save()
        return redirect("/millesimes/show")
    return render(request, 'millesimes/edit.html', {'millesimes': millesime})

def destroy(request, annee):
    millesime = Millesime.objects.get(pk=annee)
    millesime.delete()
    return redirect("/millesimes/show")
