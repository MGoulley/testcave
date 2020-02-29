# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import BenneForm
from .models import Benne
from parcelles.models import Parcelle
from django.utils.timezone import now

def create(request):
    parcelles = Parcelle.objects.all()
    if request.method == "POST":
        post = request.POST.copy()
        post.setlist("parcelles", [Parcelle.objects.get(numIlot=numIlot) for numIlot in request.POST.getlist("parcelles")])
        request.POST = post
        print(request.POST)
        form = BenneForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/bennes/show")
            except:
                pass
    else:
        form = BenneForm()
    return render(request,'bennes/index.html',{'form':form, 'lesparcelles': parcelles})

def show(request):
    bennes = Benne.objects.all()
    parcelles = Parcelle.objects.all()
    return render(request,"bennes/show.html",{'bennes':bennes, 'lesparcelles':parcelles})

def edit(request, id):
    benne = Benne.objects.get(id=id)
    parcelles = Parcelle.objects.all()
    benne.dateRecep = benne.dateRecep.strftime('%m/%d/%Y %H:%M')
    return render(request,'bennes/edit.html', {'benne':benne, 'lesparcelles': parcelles})

def update(request, id):
    benne = Benne.objects.get(id=id)
    parcelles = Parcelle.objects.all()
    print(benne)
    post = request.POST.copy()
    post.setlist("parcelles", [Parcelle.objects.get(numIlot=numIlot) for numIlot in request.POST.getlist("parcelles")])
    request.POST = post
    print(request.POST)
    # for parcelle in request.POST.getlist("parcelles"):
    #     benne.parcelles.set(parcelle)

    form = BenneForm(request.POST, instance=benne)
    if form.is_valid():
        form.save()
        return redirect("/bennes/show")
    else:
        benne = Benne.objects.get(id=id)
    return render(request, 'bennes/edit.html', {'benne': benne, 'lesparcelles': parcelles})

def destroy(request, id):
    benne = Benne.objects.get(id=id)
    benne.delete()
    return redirect("/bennes/show")

def reset(request):
    Benne.objects.all().delete()
    benne=Benne(idBenne=1, idMillesime=2021, dateRecep="2020-02-27 22:32", densite=20.8, temperature=10.2, alcProb=20.0, so2=0.25, autre1="", autre2="", meteo="AAA", pourcentSO2=0.321, idOperateur=1, idMateriel=1)
    benne.save()
    benne.parcelles.add(Parcelle.objects.all()[0])
    benne.save()
    return redirect("/bennes/show")
