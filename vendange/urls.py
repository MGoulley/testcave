# -*- encoding: utf-8 -*-

from django.urls import path, re_path, include
from . import views

MODEL_BENNE_URL_NAME = "bennes/"
MODEL_MARC_URL_NAME = "marcs/"

urlpatterns = [
    # The home page
    path(MODEL_BENNE_URL_NAME + '', views.benne_show),
    path(MODEL_BENNE_URL_NAME + 'create', views.benne_create, name="create_benne"),
    path(MODEL_BENNE_URL_NAME + 'show', views.benne_show),
    path(MODEL_BENNE_URL_NAME + 'edit/<int:id>', views.benne_edit),
    path(MODEL_BENNE_URL_NAME + 'update/<int:id>', views.benne_update),
    path(MODEL_BENNE_URL_NAME + 'delete/<int:id>', views.benne_destroy),

    path(MODEL_MARC_URL_NAME + '', views.marcs_show),
    path(MODEL_MARC_URL_NAME + 'create', views.marcs_create),
    path(MODEL_MARC_URL_NAME + 'show', views.marcs_show),
    path(MODEL_MARC_URL_NAME + 'edit/<int:id>', views.marcs_edit),
    path(MODEL_MARC_URL_NAME + 'update/<int:id>', views.marcs_update),
    path(MODEL_MARC_URL_NAME + 'delete/<int:id>', views.marcs_destroy), 
]
