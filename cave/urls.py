# -*- encoding: utf-8 -*-

from django.urls import path, re_path, include
from . import views

MODEL_LOT_URL_NAME = "lots/"

urlpatterns = [
    # The home page
    path(MODEL_LOT_URL_NAME + '', views.lot_show),
    path(MODEL_LOT_URL_NAME + 'create', views.lot_create),
    path(MODEL_LOT_URL_NAME + 'show', views.lot_show),
    path(MODEL_LOT_URL_NAME + 'edit/<int:id>', views.lot_edit),
    path(MODEL_LOT_URL_NAME + 'update/<int:id>', views.lot_update),
    path(MODEL_LOT_URL_NAME + 'delete/<int:id>', views.lot_destroy),
]
