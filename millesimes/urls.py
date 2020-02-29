# -*- encoding: utf-8 -*-

from django.urls import path, re_path, include
from . import views

urlpatterns = [
    # The home page
    path('', views.show),
    path('create', views.create),
    path('show', views.show),
    path('edit/<int:annee>', views.edit),
    path('update/<int:annee>', views.update),
    path('delete/<int:annee>', views.destroy),
]
