# -*- encoding: utf-8 -*-

from django.urls import path, re_path, include
from . import views

#MODEL_ORGANISATION_URL_NAME = "organisations/"
MODEL_DOMAINE_URL_NAME = "domaines/"
MODEL_MILLESIME_URL_NAME = "millesimes/"

urlpatterns = [
    path(MODEL_DOMAINE_URL_NAME + '', views.domaine_show),
    path(MODEL_DOMAINE_URL_NAME + 'create', views.domaine_create),
    path(MODEL_DOMAINE_URL_NAME + 'show', views.domaine_show),
    path(MODEL_DOMAINE_URL_NAME + 'edit/<int:id>', views.domaine_edit),
    path(MODEL_DOMAINE_URL_NAME + 'update/<int:id>', views.domaine_update),
    path(MODEL_DOMAINE_URL_NAME + 'delete/<int:id>', views.domaine_destroy),

    path(MODEL_MILLESIME_URL_NAME + '', views.millesime_show),
    path(MODEL_MILLESIME_URL_NAME + 'create', views.millesime_create),
    path(MODEL_MILLESIME_URL_NAME + 'show', views.millesime_show),
    path(MODEL_MILLESIME_URL_NAME + 'edit/<int:annee>', views.millesime_edit),
    path(MODEL_MILLESIME_URL_NAME + 'update/<int:annee>', views.millesime_update),
    path(MODEL_MILLESIME_URL_NAME + 'delete/<int:annee>', views.millesime_destroy)
]