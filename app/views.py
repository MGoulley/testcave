# -*- encoding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from .forms import LoginForm, SignUpForm
from administration.models import Millesime
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.core import serializers

def index(request):
    return render(request, "index.html")

def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        template = loader.get_template('pages/' + load_template)
        return HttpResponse(template.render(context, request))

    except:

        template = loader.get_template( 'pages/error-404.html' )
        return HttpResponse(template.render(context, request))

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = 'Sign in with credentials'

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                try:
                    # Organisation
                    orga = User.objects.get(pk=user.id).personnels.orga
                    request.session['organisation_id'] = orga.id
                    request.session['organisation_nom'] = orga.nom
                    # Domaines
                    domaines = orga.domaines.all()
                    domaines_id = [d.id for d in domaines]
                    domaines_name = [d.nom for d in domaines]
                    request.session['domaines'] = list(zip(domaines_id, domaines_name))
                    # Dernier millesime
                    lesmil = Millesime.objects.all().filter(orga=orga.id).order_by("-annee")
                    if len(lesmil) > 0:
                        request.session['millesime'] = lesmil[0].annee
                    else:
                        request.session['millesime'] = None
                except:
                    print("ERR")
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

def register_user(request):

    msg = 'Add your credentials'

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            return redirect("/login/")
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg" : msg})
