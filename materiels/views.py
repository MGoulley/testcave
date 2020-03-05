# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MaterielsForm
from .models import Materiels

@login_required(login_url="/login/")
def create(request):
    if request.method == "POST":
        form = MaterielsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/materiels/show")
            except:
                pass
    else:
        form = MaterielsForm()
    return render(request,'materiels/index.html',{'form':form})

@login_required(login_url="/login/")
def show(request):
    materiels = Materiels.objects.all()
    return render(request,"materiels/show.html",{'materiels':materiels})

@login_required(login_url="/login/")
def edit(request, id):
    materiel = Materiels.objects.get(id=id)
    return render(request,'materiels/edit.html', {'materiel':materiel})

@login_required(login_url="/login/")
def update(request, id):
    materiel = Materiels.objects.get(id=id)
    form = MaterielsForm(request.POST, instance = materiel)
    if form.is_valid():
        form.save()
        return redirect("/materiels/show")
    return render(request, 'materiels/edit.html', {'materiels': materiel})

@login_required(login_url="/login/")
def destroy(request, id):
    materiel = Materiels.objects.get(id=id)
    materiel.delete()
    return redirect("/materiels/show")
