# -*- encoding: utf-8 -*-

from django.urls import path, re_path, include
from . import views
from .models import *
from .views import ParcelleAutocomplete

MODEL_PARCELLE_URL_NAME = "parcelles/"
MODEL_MATERIEL_URL_NAME = "materiels/"

urlpatterns = [
    # The home page
    path(MODEL_PARCELLE_URL_NAME + '', views.parcelle_show),
    path(MODEL_PARCELLE_URL_NAME + 'create', views.parcelle_create),
    path(MODEL_PARCELLE_URL_NAME + 'show', views.parcelle_show),
    path(MODEL_PARCELLE_URL_NAME + 'edit/<int:id>', views.parcelle_edit),
    path(MODEL_PARCELLE_URL_NAME + 'update/<int:id>', views.parcelle_update),
    path(MODEL_PARCELLE_URL_NAME + 'delete/<int:id>', views.parcelle_destroy),
    path(
        MODEL_PARCELLE_URL_NAME + 'parcelle-autocomplete/',
        views.ParcelleAutocomplete.as_view(model=Parcelle),
        name='parcelle-autocomplete',
    ),
    path(
        MODEL_PARCELLE_URL_NAME + 'parcelle-autocomplete/<str:q>',
        views.ParcelleAutocomplete.as_view(model=Parcelle),
        name='parcelle-autocomplete',
    ),
    

    path(MODEL_MATERIEL_URL_NAME + '', views.materiel_show),
    path(MODEL_MATERIEL_URL_NAME + 'create', views.materiel_create),
    path(MODEL_MATERIEL_URL_NAME + 'show', views.materiel_show),
    path(MODEL_MATERIEL_URL_NAME + 'edit/<int:id>', views.materiel_edit),
    path(MODEL_MATERIEL_URL_NAME + 'update/<int:id>', views.materiel_update),
    path(MODEL_MATERIEL_URL_NAME + 'delete/<int:id>', views.materiel_destroy),
]
