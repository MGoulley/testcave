# -*- encoding: utf-8 -*-

from django.urls import path, re_path, include
from . import views

urlpatterns = [
    # The home page
    path('', views.show),
    path('create', views.create),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('reset', views.reset),
]
